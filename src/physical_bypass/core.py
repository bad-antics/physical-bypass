"""Physical Security Bypass Research"""
import json,hashlib,time
from datetime import datetime

class AccessControlAnalyzer:
    CARD_VULNERABILITIES={
        "HID_prox":{"freq":"125kHz","encryption":"None","clone_difficulty":"Easy","tools":["Proxmark3","Flipper Zero"]},
        "EM4100":{"freq":"125kHz","encryption":"None","clone_difficulty":"Easy","tools":["Proxmark3","T5577 card"]},
        "MIFARE_Classic":{"freq":"13.56MHz","encryption":"Crypto-1 (broken)","clone_difficulty":"Medium","tools":["Proxmark3","MFOC"]},
        "DESFire":{"freq":"13.56MHz","encryption":"AES-128","clone_difficulty":"Hard","tools":["Requires key extraction"]},
        "iCLASS":{"freq":"13.56MHz","encryption":"3DES/AES","clone_difficulty":"Medium-Hard","tools":["Proxmark3","iCopy-X"]},
    }
    
    def assess_card_system(self,card_type):
        return self.CARD_VULNERABILITIES.get(card_type,{"error":"Unknown card type"})
    
    def assess_facility(self,features):
        score=0
        checks={"perimeter_fence":10,"security_cameras":10,"access_control":15,"guard_staff":15,
                "visitor_management":10,"tailgate_detection":10,"intrusion_alarm":10,"lighting":5,
                "badge_policy":10,"security_training":5}
        findings=[]
        for check,points in checks.items():
            if features.get(check): score+=points
            else: findings.append({"missing":check,"points":points})
        return {"score":score,"max":100,"rating":"STRONG" if score>=80 else "MODERATE" if score>=50 else "WEAK","gaps":findings}

class LockAnalyzer:
    BYPASS_TECHNIQUES={
        "pin_tumbler":["single pin picking","raking","bump key","snap gun","impressioning"],
        "wafer":["jigglers","bypass tools","shims"],
        "disc_detainer":["DD pick (Sparrows)","custom picks"],
        "electronic":["relay attack","signal amplification","default codes","firmware exploit"],
        "smart":["Bluetooth sniffing","replay attack","firmware downgrade","API exploitation"],
    }
    
    def analyze_lock(self,lock_type,grade=None):
        techniques=self.BYPASS_TECHNIQUES.get(lock_type,[])
        return {"lock_type":lock_type,"grade":grade,"bypass_techniques":techniques,
                "resistance":"HIGH" if grade=="1" else "MEDIUM" if grade=="2" else "LOW"}
    
    def recommend_upgrades(self,current_lock):
        return ["Upgrade to ANSI Grade 1","Add electronic access control","Install security cameras at entry",
                "Implement anti-pick pins (spool/serrated)","Add deadbolt with anti-bump","Consider smart lock with audit trail"]
