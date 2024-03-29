from django.shortcuts import render
from Masters.forms import ProductsMasterForm,ProductRiskForm,AgentCreateForm
from django.contrib.auth.decorators import login_required
from Masters.models import XxgenProductRiskMaster
from django.forms import modelformset_factory
# Create your views here.


@login_required(login_url='/MyAdmin/clogin/')
def ProductsMaster(request):
    Pform = ProductsMasterForm(request.POST or None)
    if Pform.is_valid():
        form = Pform.save(commit=False)
        form.created_by = str(request.user)
        form.last_updated_by = str(request.user)
        form.save()
        Pform = ProductsMasterForm()
    context = {'Pform': Pform}
    return render(request, 'Masters/ProductMaster.html', context)

def ProductRisk(request):
    cformset = modelformset_factory(XxgenProductRiskMaster, form=ProductRiskForm, extra=4)
    formset = cformset(request.POST or None)

    if request.method == 'GET':
        search_id = request.GET.get('Sid')
        if request.GET.get('Sid') != "None" :
            try:
                formset = cformset(request.POST or None,
                                   queryset=XxgenProductRiskMaster.objects.filter(prod_code=search_id)
                                   )
            except XxgenProductRiskMaster.DoesNotExist:
                formset = cformset(queryset=XxgenProductRiskMaster.objects.none())

    if request.method == 'POST':
        if formset.is_valid():
            for form in formset.forms:
                if form['risk_code'].value() != '':
                    for name, field in form.fields.items():
                        tmpform = form.save(commit=False)
                        setattr(tmpform, 'created_by', str(request.user))
                        setattr(tmpform, 'last_updated_by', str(request.user))
                        tmpform.save()
            formset = cformset(queryset=XxgenProductRiskMaster.objects.none())

    context = {'formset':formset}
    return render(request, 'Masters/ProdRiskDetails.html', context)

def createAgent(request):
    Aform = AgentCreateForm(request.POST or None)
    if Aform.is_valid():
        form = Aform.save(commit=False)
        form.created_by = str(request.user)
        form.last_updated_by = str(request.user)
        form.save()
        Aform = AgentCreateForm()
    context = {'Aform':Aform}
    return render(request, 'Masters/AgentCreate.html', context)

from Masters.models import Xxgen_agent_Prod_Comm_Master
from Masters.forms import AgentCommisionForm

def AgentCommision(request):
    cformset = modelformset_factory(Xxgen_agent_Prod_Comm_Master, form=AgentCommisionForm, extra=5)
    formset = cformset(request.POST or None)

    if request.method == 'GET':
        search_id = request.GET.get('Sid')
        print('search_id', search_id)
        if request.GET.get('Sid') != "None" :
            try:
                formset = cformset(request.POST or None,
                                   queryset=Xxgen_agent_Prod_Comm_Master.objects.filter(agen_id=search_id)
                                   )
            except XxgenProductRiskMaster.DoesNotExist:
                formset = cformset(queryset=Xxgen_agent_Prod_Comm_Master.objects.none())

    if formset.is_valid():
        for form in formset.forms:
            if form['agen_id'].value() != '':
                for name, field in form.fields.items():
                    tmpform = form.save(commit=False)
                    setattr(tmpform, 'created_by', str(request.user))
                    setattr(tmpform, 'last_updated_by', str(request.user))
                    tmpform.save()

    context = {'formset':formset}
    return render(request, 'Masters/AgentCommission.html', context)

from Masters.forms import VehicleMasterForm,VehicleDepriciatinoForm

def VehicleMasterView(request):
    vform = VehicleMasterForm(request.POST or None)
    print('vform', vform)
    if vform.is_valid():
        form = vform.save(commit=False)
        form.created_by = str(request.user)
        form.last_updated_by = str(request.user)
        form.save()
        vform = VehicleMasterForm()
    context = {'vform': vform}
    print('vform',vform)
    return render(request, 'Masters/VehicleMaster.html', context)

def VehicleDepriciationMasterView(request):
    vform = VehicleDepriciatinoForm(request.POST or None)
    print('vform', vform)
    if vform.is_valid():
        form = vform.save(commit=False)
        form.created_by = str(request.user)
        form.last_updated_by = str(request.user)
        form.save()
        vform = VehicleDepriciatinoForm()
    context = {'vform': vform}
    print('vform',vform)
    return render(request, 'Masters/VehicleDepriciation.html', context)

from Masters.forms import  XxgenNcbMasterForm

@login_required(login_url='/MyAdmin/clogin/')
def XxgenNcbMasterView(request):

    vform = XxgenNcbMasterForm(request.POST or None)
    print('vform', vform)
    if vform.is_valid():
        form = vform.save(commit=False)
        form.created_by = str(request.user)
        form.last_updated_by = str(request.user)
        form.save()
        vform = XxgenNcbMasterForm()
    context = {'vform': vform}
    return render(request, 'Masters/NCBMaster.html', context)

from Masters.forms import ClaimStatusMasterForm

def ClaimStatusMasterView(request):

    vform = ClaimStatusMasterForm(request.POST or None)
    if vform.is_valid():
        form = vform.save(commit=False)
        form.created_by = str(request.user)
        form.last_updated_by = str(request.user)
        form.save()
        vform = ClaimStatusMasterForm()
    context = {'vform': vform}
    return render(request, 'Masters/ClaimStatus.html', context)

from Masters.forms import ClaimsSurveyorMasterForm

def ClaimsSurveyorMasterView(request):
    vform = ClaimsSurveyorMasterForm(request.POST or None)
    print('vform', vform)
    if vform.is_valid():
        form = vform.save(commit=False)
        form.created_by = str(request.user)
        form.last_updated_by = str(request.user)
        form.save()
        vform = ClaimsSurveyorMasterForm()
    context = {'vform': vform}
    print('vform', vform)
    return render(request, 'Masters/SurveyorMaster.html', context)

from Masters.models import XxgenClaimStatusMaster
from django.views.generic import ListView

class ClaimStatusListView(ListView):

    template_name = 'XxgenClaimStatusMaster_list.html'
    queryset = XxgenClaimStatusMaster.objects.all()
