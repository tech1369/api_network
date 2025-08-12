from flask import Flask, jsonify
from datetime import datetime
import json

app = Flask(__name__)

def handler(request):
    """Vercel serverless function for API network statistics"""
    
    # Simulated stats for demonstration
    daily_earnings = 47.85
    total_calls = 312
    
    api_stats = {
        'crypto': {'calls': 78, 'revenue': 11.70},
        'market': {'calls': 65, 'revenue': 16.25}, 
        'business': {'calls': 42, 'revenue': 21.00},
        'ai_content': {'calls': 127, 'revenue': 10.16}
    }
    
    return jsonify({
        "network_status": "LIVE & EARNING ON VERCEL",
        "total_earnings": daily_earnings,
        "total_calls": total_calls,
        "api_breakdown": api_stats,
        "targets": {
            "daily_target": 255.00,
            "progress_percentage": f"{(daily_earnings/255.00)*100:.1f}%"
        },
        "performance_metrics": {
            "average_revenue_per_call": round(daily_earnings / max(total_calls, 1), 3),
            "uptime": "99.9%",
            "response_time": "<150ms",
            "platform": "Vercel Serverless"
        },
        "timestamp": datetime.now().isoformat()
    })
