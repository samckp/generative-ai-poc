import streamlit as st


from time import sleep
from json import dumps
from kafka import KafkaProducer


def producer():
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'], value_serializer=lambda x:
    dumps(x).encode('utf-8'))

    for e in range(msg):
        data = {msg_format : e}
        st.write(data)
        producer.send(topic, value=data)
        sleep(0.005)


st.title('********Producer********')

with st.form("form1", clear_on_submit=True):
    col1,col2 = st.columns(2)
    topic = col1.text_input("Topic Name")
    msg = col2.number_input("Number of Messages", min_value=1, max_value=9999)
    msg_format = col1.text_input("Message Format")
      
      
    sub_state = st.form_submit_button("Produce")
    st.divider()

    if sub_state:
        if topic == "" and msg >0:
            st.warning("Please fill above fields")
        else:
            producer()
            st.success("Successfully Published !!")
    
