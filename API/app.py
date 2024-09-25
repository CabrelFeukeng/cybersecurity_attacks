from pydantic import BaseModel
import numpy as np
import pandas as pd
import joblib
from flask import Flask, request, jsonify
from datetime import datetime

modelV1 = joblib.load("modelV1.pkl")
modelV2 = joblib.load("modelV1.pkl")

def date_to_seconde(time_str):
    time_obj = datetime.strptime(time_str, '%H:%M:%S')
    total_seconds = time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second
    return total_seconds

def remove_dots(ip_address):
    return ip_address.replace('.', '')

AttackSignatureDic = {
    "Known Pattern A" : 0,
    "Known Pattern B": 1
}

ActionTakenDic = {
    "Blocked" : 0,
    "Ignored"  : 1,
    "Logged" : 2
}

PacketTypeDic = {
    "Control" : 0,
    "Data" : 1
}

SeverityLevelDic = {
    "High" : 0,
    "Low" : 1,
    "Medium" : 2
}

ProtocolDic = {
    "ICMP" : 0,
    "TCP" : 1,
    "UDP" : 2
}

NetworkSegmentDic = {
    "Segment A" : 0,
    "Segment B" : 1,
    "Segment C" : 2
}

FirewallLogsDic =  {
    "Log Data" : 0,
    "Not Log" : 1
}

LogSourceDic = {
    "Firewall" : 0,
    "Server" : 1
}

TrafficTypeDic = {
    "DNS" : 0,
    "FTP" : 1,
    "HTTP" : 2
}

AttackTypeDic = {
    "DDos" : 0,
    "Intrusion" : 1,
    "Malware" : 2
}



class InputData(BaseModel):
    Timestamp: str
    SourceIPAddress: float
    DestinationIPAddress: float
    SourcePort: float
    DestinationPort: float
    Protocol: str
    PacketType: str
    PacketLength: float
    TrafficType: str
    AnomalyScores: float
    AttackType: str
    AttackSignature: str
    ActionTaken: str
    SeverityLevel: str
    NetworkSegment: str
    FirewallLogs: str
    LogSource: str

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    input_data = InputData(**data)
    print(PacketTypeDic[input_data.PacketType])
    prediction = modelV1.predict([[date_to_seconde(input_data.Timestamp), 
                                   remove_dots(input_data.SourceIPAddress),
                                   remove_dots(input_data.DestinationIPAddress),
                                   input_data.SourcePort,
                                   input_data.DestinationPort,
                                   ProtocolDic[input_data.Protocol],
                                   PacketTypeDic[input_data.PacketType],
                                   input_data.PacketLength,
                                   TrafficTypeDic[input_data.TrafficType],
                                   input_data.AnomalyScores,
                                   AttackSignatureDic[input_data.AttackSignature],
                                   AttackTypeDic[input_data.AttackType],
                                   ActionTakenDic[input_data.ActionTaken],
                                   SeverityLevelDic[input_data.SeverityLevel],
                                   FirewallLogsDic[input_data.FirewallLogs],
                                   NetworkSegmentDic[input_data.NetworkSegment],
                                   LogSourceDic[input_data.LogSource]
                                   ]])
    return jsonify({"prediction": prediction[0]})

if __name__ == "__main__":
    app.run(debug=True, port=5000)