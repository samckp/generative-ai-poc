import streamlit as st


from time import sleep
from json import dumps
from kafka import KafkaProducer

st.title('Producer')

topic_name='mytopic'
producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x:
dumps(x).encode('utf-8'))

for e in range(10):
    data = {'number' : e}
    print(data)
    producer.send(topic_name, value=data)
    sleep(0.005)