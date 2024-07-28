from django.shortcuts import render
from django.http import JsonResponse
from .forms import FormIdentifikasiDonor
import joblib
import numpy as np

def home(request):
    return render(request, 'identifikasi_donor/home.html')

def about(request):
    return render(request, 'identifikasi_donor/about.html')

def identification(request):
    if request.method == 'POST':
        form = FormIdentifikasiDonor(request.POST)
        if form.is_valid():
            # Load model dan scaler
            model = joblib.load('best_model.pkl')
            scaler = joblib.load('scaler.pkl')
            
            # Siapkan data input
            input_data = np.array([[
                form.cleaned_data['age'],
                form.cleaned_data['hemoglobin'],
                form.cleaned_data['weight'],
                form.cleaned_data['systolic'],
                form.cleaned_data['diastolic']
            ]])
            
            # Normalisasi input data
            input_scaled = scaler.transform(input_data)
            
            # Make prediction
            prediction = model.predict(input_scaled)[0]
            prediction_result = "Eligible" if prediction == 1 else "Not Eligible"
            icon = "success" if prediction == 1 else "warning"

            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return JsonResponse({
                    'prediksi': prediction_result,
                    'icon': icon
                })
            else:
                return render(request, 'identifikasi_donor/identification.html', {
                    'form': form,
                    'prediksi': prediction_result
                })
    else:
        form = FormIdentifikasiDonor()
    return render(request, 'identifikasi_donor/identification.html', {'form': form})