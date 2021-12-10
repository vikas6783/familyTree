from django.db import models
from django.db.models.deletion import CASCADE
from phonenumber_field.modelfields import PhoneNumberField

# job location


class JobLocation(models.Model):
    address_line1 = models.CharField(max_length=30, blank=False)
    address_line2 = models.CharField(max_length=30, blank=True)
    landmark = models.CharField(max_length=30, blank=False)
    city = models.CharField(max_length=30, blank=False)
    state = models.CharField(max_length=30, blank=False)
    pincode = models.CharField(max_length=30, blank=False)

    class Meta:
        db_table = "job_location"

    def __str__(self):
        return self.address_line1

# job details


class JobDetail(models.Model):
    occupation = models.CharField(max_length=30, blank=True)
    years_of_experience = models.IntegerField(blank=False)
    company_name = models.CharField(max_length=30, blank=True)
    job_location = models.ForeignKey(JobLocation, on_delete=CASCADE)

    class Meta:
        db_table = "job_detail"

    def __str__(self):
        return self.occupation

# family address


class FamilyAddress(models.Model):
    address_line1 = models.CharField(max_length=30, blank=False)
    address_line2 = models.CharField(max_length=30, blank=True)
    landmark = models.CharField(max_length=30, blank=False)
    city = models.CharField(max_length=30, blank=False)
    state = models.CharField(max_length=30, blank=False)
    pincode = models.CharField(max_length=30, blank=False)

    class Meta:
        db_table = "family_address"

    def __str__(self):
        return self.address_line1


class CollegeAddress(models.Model):
    area = models.CharField(max_length=30, blank=False)
    city = models.CharField(max_length=30, blank=False)
    state = models.CharField(max_length=30, blank=False)
    pincode = models.CharField(max_length=30, blank=False)
    country = models.CharField(max_length=30, blank=False)

    class Meta:
        db_table = "college_address"

    def __str__(self):
        return self.area


class EducationDetail(models.Model):
    qualification = models.CharField(max_length=50, blank=False)
    college = models.CharField(max_length=50, blank=False)
    year_of_completion = models.IntegerField(blank=False)
    college_address = models.ForeignKey(CollegeAddress, on_delete=CASCADE)

    class Meta:
        db_table = "education_detail"

    def __str__(self):
        return self.college

# basic details


class Person(models.Model):
    family_name = models.CharField(max_length=30, blank=False)
    first_name = models.CharField(max_length=30, blank=False)
    last_name = models.CharField(max_length=30, blank=False)
    date_of_birth = models.DateField(blank=False)
    blood_group = models.CharField(max_length=5, blank=False)
    age = models.IntegerField(blank=False)
    GENDER = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    ]
    gender = models.CharField(max_length=10)
    models.CharField(blank=False, choices=gender.choices, max_length=10)

    phone_number = PhoneNumberField(blank=False)
    aadhar_card = models.CharField(max_length=50, blank=False)
    pan_card = models.CharField(max_length=50, blank=False)

    job_detail = models.ForeignKey(JobDetail, on_delete=CASCADE)
    address = models.ForeignKey(FamilyAddress, on_delete=CASCADE)
    education_detail = models.ForeignKey(EducationDetail, on_delete=CASCADE)

    class Meta:
        db_table = "person"

    def __str__(self):
        return self.first_name
