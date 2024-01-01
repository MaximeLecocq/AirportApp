# Import modules

from django.shortcuts import render,redirect
from rest_framework import viewsets,filters
from rest_framework.pagination import PageNumberPagination
from .serializers import AirportSerializer
from .models import Airport
from .forms import AirportForm
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger



#################################################################
############################ Classes ############################
#################################################################

class AirportPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    pagination_class = AirportPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['airport_name', 'country', 'airport_type', 'continent']


################# Classes for airport types #################

class LargeAirportsViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.filter(airport_type='large airport')
    serializer_class = AirportSerializer

class MediumAirportsViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.filter(airport_type='medium airport')
    serializer_class = AirportSerializer

class SmallAirportsViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.filter(airport_type='small airport')
    serializer_class = AirportSerializer

class HeliportsViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.filter(airport_type='heliport')
    serializer_class = AirportSerializer

class SeaplaneBasesViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.filter(airport_type='seaplane base')
    serializer_class = AirportSerializer


################# Classes for continents #################

class AsiaViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.filter(continent='Asia')
    serializer_class = AirportSerializer

class AfricaViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.filter(continent='Africa')
    serializer_class = AirportSerializer

class OceaniaViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.filter(continent='Oceania')
    serializer_class = AirportSerializer

class SouthCentralAmericaViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.filter(continent='South and Central America')
    serializer_class = AirportSerializer

class EuropeViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.filter(continent='Europe')
    serializer_class = AirportSerializer

class NorthAmericaViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.filter(continent='NorthAmerica')
    serializer_class = AirportSerializer



#################################################################
###################### CRUD Functionality  ######################
#################################################################


# CREATE: Renders a form to create a new airport entry
def create_airport(request):
    form = AirportForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('airport:index')
    
    return render(request,'airport/airport-form.html',{'form':form})


# READ: Renders the index and detail pages 
def index(request):
    return render(request,'airport/index.html')

def detail(request,airport_id):
    airport = Airport.objects.get(pk=airport_id)
    context = {
        'airport':airport,
    }
    return render(request,'airport/detail.html',context)


# UPDATE: Renders a form to update an existing airport entry
def update_airport(request,airport_id):
    airport = Airport.objects.get(airport_id=airport_id)
    form = AirportForm(request.POST or None, instance = airport)

    if form.is_valid():
        form.save()
        return redirect('airport:index')
    
    return render(request,'airport/airport-form.html',{'form':form, 'airport':airport})


# DELETE: Deletes an existing airport entry
def delete_airport(request,airport_id):
    airport = Airport.objects.get(airport_id=airport_id)

    if request.method == 'POST':
        airport.delete()
        return redirect('airport:airport')
    
    return render(request,'airport/airport-delete.html',{'airport':airport})



#################################################################
###################### View functions for  ######################
#################################################################

# Define view function for all airports
def airport(request):
    # Retrieve Airport objects
    airport_list = Airport.objects.all()
    
    # Get the value of 'airport_name' from request's GET parameters
    airport_name = request.GET.get('airport_name')
    
    # Check if 'airport_name' is not empty and is not None, then filter airport_list
    if airport_name != '' and airport_name is not None:
        airport_list = airport_list.filter(airport_name__icontains=airport_name)

    # Paginate the filtered airport_list, showing 10 airports per page
    paginator = Paginator(airport_list, 10)
    page = request.GET.get('page')
    
    try:
        # Try to retrieve the requested page of airports
        airports = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, show the first page
        airports = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver the last page of results
        airports = paginator.page(paginator.num_pages)

    # Pass the paginated airports to the template    
    context = {
        'airport_list': airports,
    }
    # Render the 'airport.html' template with the context data
    return render(request,'airport/airport.html',context)


# Define view function for Asia airports
def asia(request):
    # Retrieve Airport objects filtered by continent
    airport_list = Airport.objects.filter(continent="Asia")
    
    # Get the value of 'airport_name' from request's GET parameters
    airport_name = request.GET.get('airport_name')
    
    # Check if 'airport_name' is not empty and is not None, then filter airport_list
    if airport_name != '' and airport_name is not None:
        airport_list = airport_list.filter(airport_name__icontains=airport_name)

    # Paginate the filtered airport_list, showing 10 airports per page
    paginator = Paginator(airport_list, 10)
    page = request.GET.get('page')
    
    try:
        # Try to retrieve the requested page of airports
        airports = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, show the first page
        airports = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver the last page of results
        airports = paginator.page(paginator.num_pages)

    # Pass the paginated airports to the template    
    airport_asia = {
        'airport_list': airports,
    }
    # Render the 'asia.html' template with the context data
    return render(request,'airport/asia.html',airport_asia)


# Define view function for Africa airports
def africa(request):
    # Retrieve Airport objects filtered by continent
    airport_list = Airport.objects.filter(continent="Africa")
    
    # Get the value of 'airport_name' from request's GET parameters
    airport_name = request.GET.get('airport_name')
    
    # Check if 'airport_name' is not empty and is not None, then filter airport_list
    if airport_name != '' and airport_name is not None:
        airport_list = airport_list.filter(airport_name__icontains=airport_name)

    # Paginate the filtered airport_list, showing 10 airports per page
    paginator = Paginator(airport_list, 10)
    page = request.GET.get('page')
    
    try:
        # Try to retrieve the requested page of airports
        airports = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, show the first page
        airports = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver the last page of results
        airports = paginator.page(paginator.num_pages)

    # Pass the paginated airports to the template    
    airport_africa = {
        'airport_list': airports,
    }
    # Render the 'africa.html' template with the context data
    return render(request,'airport/africa.html',airport_africa)


# Define view function for Oceania airports
def oceania(request):
    # Retrieve Airport objects filtered by continent
    airport_list = Airport.objects.filter(continent="Oceania")
    
    # Get the value of 'airport_name' from request's GET parameters
    airport_name = request.GET.get('airport_name')
    
    # Check if 'airport_name' is not empty and is not None, then filter airport_list
    if airport_name != '' and airport_name is not None:
        airport_list = airport_list.filter(airport_name__icontains=airport_name)

    # Paginate the filtered airport_list, showing 10 airports per page
    paginator = Paginator(airport_list, 10)
    page = request.GET.get('page')
    
    try:
        # Try to retrieve the requested page of airports
        airports = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, show the first page
        airports = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver the last page of results
        airports = paginator.page(paginator.num_pages)

    # Pass the paginated airports to the template    
    airport_oceania = {
        'airport_list': airports,
    }
    # Render the 'oceania.html' template with the context data
    return render(request,'airport/oceania.html',airport_oceania)


# Define view function for South and Central America airports
def southandcentralamerica(request):
    # Retrieve Airport objects filtered by continent
    airport_list = Airport.objects.filter(continent="South and Central America")
    
    # Get the value of 'airport_name' from request's GET parameters
    airport_name = request.GET.get('airport_name')
    
    # Check if 'airport_name' is not empty and is not None, then filter airport_list
    if airport_name != '' and airport_name is not None:
        airport_list = airport_list.filter(airport_name__icontains=airport_name)

    # Paginate the filtered airport_list, showing 10 airports per page
    paginator = Paginator(airport_list, 10)
    page = request.GET.get('page')
    
    try:
        # Try to retrieve the requested page of airports
        airports = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, show the first page
        airports = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver the last page of results
        airports = paginator.page(paginator.num_pages)

    # Pass the paginated airports to the template    
    airport_southamerica = {
        'airport_list': airports,
    }
    # Render the 'southamerica.html' template with the context data
    return render(request,'airport/southamerica.html',airport_southamerica)


# Define view function for Antartica airports
def antartica(request):
    # Retrieve Airport objects filtered by continent
    airport_list = Airport.objects.filter(continent="Antartica")
    
    # Get the value of 'airport_name' from request's GET parameters
    airport_name = request.GET.get('airport_name')
    
    # Check if 'airport_name' is not empty and is not None, then filter airport_list
    if airport_name != '' and airport_name is not None:
        airport_list = airport_list.filter(airport_name__icontains=airport_name)

    # Paginate the filtered airport_list, showing 10 airports per page
    paginator = Paginator(airport_list, 10)
    page = request.GET.get('page')
    
    try:
        # Try to retrieve the requested page of airports
        airports = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, show the first page
        airports = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver the last page of results
        airports = paginator.page(paginator.num_pages)

    # Pass the paginated airports to the template
    airport_antartica = {
        'airport_list': airports,
    }
    # Render the 'antartica.html' template with the context data
    return render(request,'airport/southamerica.html',airport_antartica)


# Define view function for North America airports
def northamerica(request):
    # Retrieve Airport objects filtered by continent
    airport_list = Airport.objects.filter(continent="North America")
    
    # Get the value of 'airport_name' from request's GET parameters
    airport_name = request.GET.get('airport_name')

    # Check if 'airport_name' is not empty and is not None, then filter airport_list
    if airport_name != '' and airport_name is not None:
        airport_list = airport_list.filter(airport_name__icontains=airport_name)

    # Paginate the filtered airport_list, showing 10 airports per page
    paginator = Paginator(airport_list, 10)
    page = request.GET.get('page')
    
    try:
        # Try to retrieve the requested page of airports
        airports = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, show the first page
        airports = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver the last page of results
        airports = paginator.page(paginator.num_pages)

    # Pass the paginated airports to the template
    airport_northamerica = {
        'airport_list': airports,
    }
    # Render the 'northamerica.html' template with the context data
    return render(request,'airport/northamerica.html',airport_northamerica)