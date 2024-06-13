from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import UploadFile
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

def upload_file(request):
    """
    Handle file upload from the user.

    This view renders a form that allows users to upload CSV files.
    Upon successful submission, the uploaded file is saved and the user is redirected to the process_file view for data analysis.

    Args:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponse: Rendered HTML response with the file upload form.
    """
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('process_file')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def process_file(request):
    """
    Process the uploaded CSV file and perform data analysis.

    This view reads the most recently uploaded CSV file, performs basic data analysis such as displaying the first few rows,
    calculating summary statistics, and identifying missing values. It also generates histograms for numerical columns.
    The results and visualizations are then rendered on the results page.

    Args:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponse: Rendered HTML response displaying the data analysis results and visualizations.
    """
    # Get the most recent uploaded file
    uploaded_file = UploadFile.objects.latest('uploaded_at')
    file_path = uploaded_file.file.path
    
    # Read the CSV file using pandas
    df = pd.read_csv(file_path)

    # Perform basic data analysis
    summary = df.describe().to_html()
    head = df.head().to_html()
    missing_values = df.isnull().sum().to_frame(name='Missing Values').to_html()

    # Generate visualizations
    histograms = []
    for column in df.select_dtypes(include=['float64', 'int64']).columns:
        plt.figure()
        sns.histplot(df[column].dropna(), kde=True)
        buf = BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
        histograms.append(image_base64)
        buf.close()
        plt.close()

    context = {
        'summary': summary,
        'head': head,
        'missing_values': missing_values,
        'histograms': histograms,
    }
    return render(request, 'results.html', context)
