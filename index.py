from flask import Flask, jsonify
import json

app = Flask(__name__)

# Global earnings tracking for Vercel
daily_earnings = 0.0
total_calls = 0

def handler(request):
    """Vercel serverless function handler for homepage"""
    
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Deploy API Service Network</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 0; background: #f0f2f5; }}
            .container {{ max-width: 1200px; margin: 0 auto; padding: 20px; }}
            .header {{ text-align: center; background: #4267B2; color: white; padding: 40px; border-radius: 10px; }}
            .stats {{ background: white; padding: 20px; border-radius: 10px; margin: 20px 0; text-align: center; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
            .api-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 20px 0; }}
            .api-card {{ background: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
            .api-title {{ font-size: 24px; margin-bottom: 15px; color: #333; }}
            .api-price {{ color: #28a745; font-size: 28px; font-weight: bold; margin: 15px 0; }}
            .api-endpoint {{ background: #f8f9fa; padding: 15px; border-radius: 5px; font-family: monospace; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Deploy API Service Network</h1>
                <p>Premium data intelligence APIs - Powered by Vercel</p>
            </div>
            
            <div class="stats">
                <h3>Live Stats</h3>
                <p><strong>Revenue Today:</strong> ${daily_earnings:.2f}</p>
                <p><strong>API Calls Served:</strong> {total_calls}</p>
                <p><strong>Status:</strong> LIVE & EARNING ON VERCEL</p>
            </div>
            
            <div class="api-grid">
                <div class="api-card">
                    <div class="api-title">Crypto Intelligence API</div>
                    <div class="api-price">$0.15 per call</div>
                    <p>Real-time cryptocurrency market analysis and predictions.</p>
                    <div class="api-endpoint">GET /api/crypto-intelligence</div>
                </div>
                
                <div class="api-card">
                    <div class="api-title">Market Research API</div>
                    <div class="api-price">$0.25 per call</div>
                    <p>Comprehensive market research and competitor analysis.</p>
                    <div class="api-endpoint">GET /api/market-research</div>
                </div>
                
                <div class="api-card">
                    <div class="api-title">Business Intelligence API</div>
                    <div class="api-price">$0.50 per call</div>
                    <p>Advanced business analytics and growth insights.</p>
                    <div class="api-endpoint">GET /api/business-intelligence</div>
                </div>
                
                <div class="api-card">
                    <div class="api-title">AI Content API</div>
                    <div class="api-price">$0.08 per call</div>
                    <p>AI-powered content generation and optimization.</p>
                    <div class="api-endpoint">GET /api/ai-content</div>
                </div>
            </div>
            
            <div style="text-align: center; margin: 40px 0;">
                <h2>Ready to integrate our APIs?</h2>
                <p>Serverless. Scalable. Pay-per-use pricing.</p>
                <p><strong>Target Revenue: $255/day</strong></p>
            </div>
        </div>
    </body>
    </html>
    """
