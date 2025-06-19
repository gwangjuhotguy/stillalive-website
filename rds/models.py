from django.db import models

class SystemData(models.Model):
	report2_id = models.IntegerField()  # ✅ 새로 추가된 필드
	buyer_id = models.CharField(max_length=50)
	time_stamp = models.DateTimeField(primary_key=True)
	lat = models.FloatField()
	lon = models.FloatField()
	sog = models.FloatField()
	cog = models.FloatField()
	press = models.IntegerField()

	class Meta:
		db_table = 'system_data'
		managed = False
	