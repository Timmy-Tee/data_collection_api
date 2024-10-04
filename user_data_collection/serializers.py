from rest_framework import serializers
from . models import CustomerDetail
import re as regexp

class CustomerSerializer(serializers.ModelSerializer):
     customer_name = serializers.CharField(
          error_messages={
               'blank': "This Field Cannot Be Left blank. Please Enter A Name",
          }
     )
     amount_paid = serializers.IntegerField(
          error_messages = {
               'invalid': "Amount Paid Should Be Numeric"
          }    
     )
     class Meta:
          model = CustomerDetail
          fields = ['customer_name', 'location', 'amount_paid', 'volume_dispensed', 'status']
          
     
     def validate(self, incoming_data):
          # Check If The Customer Input Has A Numerical Value or Any Special Character
          if regexp.search(r'[^a-zA-Z ]', incoming_data['customer_name']):
               raise serializers.ValidationError({'customer_name': 'Name Cannot Contain Any Special Characters'})
               
          
          # Checks to see if the amount entered is less than or equal to 0
          if (incoming_data['amount_paid'] <= 0):
               raise serializers.ValidationError({'amount_paid': 'Amount Must Be Greate Than Zero'})
          
          # Checks to see if the volume entered is within the acceptable range of a predefined business
          if not(1 <= incoming_data['volume_dispensed'] <=1000 ):
               raise serializers.ValidationError({'volume_dispensed': 'Volume Must Be Between 1 and 1000 Units'})
          return(incoming_data)
