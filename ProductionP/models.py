from django.db import models

# Create your models here.

# Create your models here.

class Asset1(models.Model):
	kode_field = models.IntegerField(unique="true",primary_key="True")
	nama_field = models.CharField(max_length=100,null="False")
	Gas_Target = models.FloatField(null="False")
	Oil_Target = models.FloatField(null="False")
	OilUOM = models.CharField(default="BOpd",null="False",max_length=10)
	GasUOM = models.CharField(default="MMSCFD",null="False",max_length=10)

	def __str__(self):              # __unicode__ on Python 2
		return str(self.kode_field)+' - '+self.nama_field

class Input_Asset1(models.Model):
	date = models.DateTimeField('date published',null="False")
	id_Kode_field = models.ForeignKey(Asset1,on_delete=models.CASCADE,null="True",blank="True")
	nama_field = models.CharField(max_length=100,null="False")
	Gas_Target = models.FloatField(null="False")
	Oil_Target = models.FloatField(null="False")
	InputOil_Target = models.FloatField(null="False")
	InputGas_Target = models.FloatField(null="False")
	OilUOM = models.CharField(default="BOpd",null="False",max_length=10)
	GasUOM = models.CharField(default="MMSCFD",null="False",max_length=10)


	def __str__(self):              # __unicode__ on Python 2
		return str(self.date)

# ==============================================================================================

class Asset2(models.Model):
	kode_field = models.IntegerField(unique="true",primary_key="True")
	nama_field = models.CharField(max_length=100,null="False")
	Gas_Target = models.FloatField(null="False")
	Oil_Target = models.FloatField(null="False")
	OilUOM = models.CharField(default="BOpd",null="False",max_length=10)
	GasUOM = models.CharField(default="MMSCFD",null="False",max_length=10)

	def __str__(self):              # __unicode__ on Python 2
		return str(self.kode_field)+' - '+self.nama_field


class Input_Asset2(models.Model):
	date = models.DateTimeField('date published',null="False")
	id_Kode_field = models.ForeignKey(Asset2,on_delete=models.CASCADE,null="True",blank="True")
	nama_field = models.CharField(max_length=100,null="False")
	Gas_Target = models.FloatField(null="False")
	Oil_Target = models.FloatField(null="False")
	InputOil_Target = models.FloatField(null="False")
	InputGas_Target = models.FloatField(null="False")
	OilUOM = models.CharField(default="BOpd",null="False",max_length=10)
	GasUOM = models.CharField(default="MMSCFD",null="False",max_length=10)


	def __str__(self):              # __unicode__ on Python 2
		return str(self.date)

# ==============================================================================================

class Asset3(models.Model):
	kode_field = models.IntegerField(unique="true",primary_key="True")
	nama_field = models.CharField(max_length=100,null="False")
	Gas_Target = models.FloatField(null="False")
	Oil_Target = models.FloatField(null="False")
	OilUOM = models.CharField(default="BOpd",null="False",max_length=10)
	GasUOM = models.CharField(default="MMSCFD",null="False",max_length=10)

	def __str__(self):              # __unicode__ on Python 2
		return str(self.kode_field)+' - '+self.nama_field


class Input_Asset3(models.Model):
	date = models.DateTimeField('date published',null="False")
	id_Kode_field = models.ForeignKey(Asset3,on_delete=models.CASCADE,null="True",blank="True")
	nama_field = models.CharField(max_length=100,null="False")
	Gas_Target = models.FloatField(null="False")
	Oil_Target = models.FloatField(null="False")
	InputOil_Target = models.FloatField(null="False")
	InputGas_Target = models.FloatField(null="False")
	OilUOM = models.CharField(default="BOpd",null="False",max_length=10)
	GasUOM = models.CharField(default="MMSCFD",null="False",max_length=10)


	def __str__(self):              # __unicode__ on Python 2
		return str(self.date)

# ==============================================================================================

class Asset4(models.Model):
	kode_field = models.IntegerField(unique="true",primary_key="True")
	nama_field = models.CharField(max_length=100,null="False")
	Gas_Target = models.FloatField(null="False")
	Oil_Target = models.FloatField(null="False")
	OilUOM = models.CharField(default="BOpd",null="False",max_length=10)
	GasUOM = models.CharField(default="MMSCFD",null="False",max_length=10)

	def __str__(self):              # __unicode__ on Python 2
		return str(self.kode_field)+' - '+self.nama_field


class Input_Asset4(models.Model):
	date = models.DateTimeField('date published',null="False")
	id_Kode_field = models.ForeignKey(Asset4,on_delete=models.CASCADE,null="True",blank="True")
	nama_field = models.CharField(max_length=100,null="False")
	Gas_Target = models.FloatField(null="False")
	Oil_Target = models.FloatField(null="False")
	InputOil_Target = models.FloatField(null="False")
	InputGas_Target = models.FloatField(null="False")
	OilUOM = models.CharField(default="BOpd",null="False",max_length=10)
	GasUOM = models.CharField(default="MMSCFD",null="False",max_length=10)


	def __str__(self):              # __unicode__ on Python 2
		return str(self.date)

# ==============================================================================================

class Asset5(models.Model):
	kode_field = models.IntegerField(unique="true",primary_key="True")
	nama_field = models.CharField(max_length=100,null="False")
	Gas_Target = models.FloatField(null="False")
	Oil_Target = models.FloatField(null="False")
	OilUOM = models.CharField(default="BOpd",null="False",max_length=10)
	GasUOM = models.CharField(default="MMSCFD",null="False",max_length=10)

	def __str__(self):              # __unicode__ on Python 2
		return str(self.kode_field)+' - '+self.nama_field


class Input_Asset5(models.Model):
	date = models.DateTimeField('date published',null="False")
	id_Kode_field = models.ForeignKey(Asset5,on_delete=models.CASCADE,null="True",blank="True")
	nama_field = models.CharField(max_length=100,null="False")
	Gas_Target = models.FloatField(null="False")
	Oil_Target = models.FloatField(null="False")
	InputOil_Target = models.FloatField(null="False")
	InputGas_Target = models.FloatField(null="False")
	OilUOM = models.CharField(default="BOpd",null="False",max_length=10)
	GasUOM = models.CharField(default="MMSCFD",null="False",max_length=10)


	def __str__(self):              # __unicode__ on Python 2
		return str(self.date)

