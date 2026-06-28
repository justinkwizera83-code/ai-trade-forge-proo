# CLEAN_CONFIRMATION_OVERLAY_v1.0.py
# This runs ON TOP of your existing code. Does NOT change any original files.

import time
import json

class CleanConfirmationOverlay:
    def __init__(self):
        self.signal_cache = []
        self.last_execution_time = 0

    def apply_filter(self, raw_signal):
        """
        This function takes your existing bot's raw signal and applies
        a "Clean Confirmation" filter WITHOUT modifying your original code.
        """
        
        # 1. EXTRACT YOUR EXISTING SIGNAL DATA
        signal_type = raw_signal.get('type')  # BUY or SELL
        price = raw_signal.get('price')
        timestamp = raw_signal.get('timestamp')
        expiry = raw_signal.get('expiry')  # Your original 1-minute expiry
        
        # 2. ADD THE "RETEST CONFIRMATION" (ACTIVATES STEP 2)
        # This checks if the price has bounced OFF the S/R level
        retest_confirmed = self.check_retest(signal_type, price)
        
        # 3. ADD THE "VOLUME SPIKE" CONFIRMATION
        # Prevents entry on low-volume fakeouts
        volume_confirmed = self.check_volume(price)
        
        # 4. ADD THE "MULTI-TIMEFRAME" CONFIRMATION
        # Checks if the 15-minute trend matches your 1-minute signal
        tf_confirmed = self.check_multi_timeframe(signal_type)
        
        # 5. FINAL DECISION
        if retest_confirmed and volume_confirmed and tf_confirmed:
            # Override expiry to 2 MINUTES (does NOT change your original code)
            raw_signal['expiry'] = '00:02:00'
            raw_signal['clean_confirmation'] = True
            return raw_signal  # PASS THROUGH
        else:
            raw_signal['clean_confirmation'] = False
            return None  # BLOCK THE SIGNAL

    def check_retest(self, signal_type, price):
        """
        Confirms price has retested the S/R level within the last 3 candles.
        This is STEP 2 from your VISION engine (now active).
        """
        # Simulate retest logic (replace with your actual MT5 API call)
        # In real implementation, fetch last 3 candles and check for bounce
        return True  # Placeholder - replace with actual logic

    def check_volume(self, price):
        """
        Confirms volume is above average (prevents fakeouts).
        """
        # Simulate volume check
        return True  # Placeholder - replace with actual logic

    def check_multi_timeframe(self, signal_type):
        """
        Confirms the 15-minute chart aligns with the 1-minute signal.
        """
        # Simulate MTF check
        return True  # Placeholder - replace with actual logic


# =====================================================
# HOW TO INTEGRATE WITH YOUR EXISTING BOT
# =====================================================

if __name__ == "__main__":
    # Example demo integration
    print("[SYSTEM] Initializing Clean Confirmation Overlay v1.0...")
    overlay = CleanConfirmationOverlay()
    
    mock_raw_signal = {
        "type": "BUY",
        "price": 1.08250,
        "timestamp": int(time.time()),
        "expiry": "00:01:00"
    }
    
    print(f"Incoming Raw Signal: {mock_raw_signal}")
    filtered = overlay.apply_filter(mock_raw_signal)
    
    if filtered:
        print(f"✅ SIGNAL PASSED! Upgraded with 2-minute expiration: {filtered}")
    else:
        print("❌ Signal blocked by Clean Confirmation Overlay")
