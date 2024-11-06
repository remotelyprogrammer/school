from django.shortcuts import render, get_object_or_404, redirect
from .forms import StudentForm, ContactFormSet, AddressFormSet, AddressForm, ContactForm
from .models import Student, Address, Contact
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse

def home(request):
    return render(request, 'students/base.html')

class CreateStudentView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/create-student.html'
    success_url = reverse_lazy('students:student-home')

    def get_context_data(self, **kwargs):
        context = super(CreateStudentView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['contact_formset'] = ContactFormSet(self.request.POST)
            context['address_formset'] = AddressFormSet(self.request.POST)
        else:
            context['contact_formset'] = ContactFormSet()
            context['address_formset'] = AddressFormSet()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        address_formset = context['address_formset']
        contact_formset = context['contact_formset']
        if form.is_valid() and address_formset.is_valid() and contact_formset.is_valid():
            self.object = form.save()
            address_formset.instance = self.object
            address_formset.save()
            contact_formset.instance = self.object
            contact_formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form))
        
def add_or_update_address(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    # Check if the student already has an address
    try:
        address = student.address  # OneToOneField allows direct access
    except Address.DoesNotExist:
        address = None

    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            address = form.save(commit=False)
            address.student = student  # Associate the address with the student
            address.save()
            return redirect('students:student_detail', student_id=student.pk)
    else:
        form = AddressForm(instance=address)

    return render(request, 'students/add_or_update_address.html', {'form': form, 'student': student})

def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    print(f"Student ID: {student.pk}")  # Debugging log
    return render(request, 'students/student_detail.html', {'student': student})

class AddContactView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'students/add_contact.html'

    # Override this method to inject the student into the form
    def form_valid(self, form):
        student_id = self.kwargs['student_id']
        student = Student.objects.get(pk=student_id)
        form.instance.student = student  # Link the contact to the student
        return super().form_valid(form)

    # Redirect the user to the student detail page after successful submission
    def get_success_url(self):
        return reverse('students:student_detail', kwargs={'student_id': self.kwargs['student_id']})