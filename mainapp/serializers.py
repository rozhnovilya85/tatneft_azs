from rest_framework import serializers

class Tatneft_azs(serializers.Serializer):
    number_azs = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length=250)
    latitude = serializers.DecimalField(max_digits=12, decimal_places=10)
    longitude = serializers.DecimalField(max_digits=12, decimal_places=10)
    DT = serializers.CharField(max_length=20)
    DT_Taneko = serializers.CharField(max_length=20)
    DT_winter = serializers.CharField(max_length=20)
    DT_arctic = serializers.CharField(max_length=20)


