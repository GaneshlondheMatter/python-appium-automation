# import os
# import time
# from dotenv import load_dotenv
# from utils.db_connection import DBConnection

# load_dotenv()

# class OTPHelper:

#     @staticmethod
#     def get_latest_otp(phone_number):
#         """Fetch the latest OTP from the database for the given phone number."""
#         connection = DBConnection.get_connection()
#         cursor = connection.cursor()

#         # ✅ FIXED QUERY (use correct column: time_stamp)
#         query = """
#         SELECT otp
#         FROM public.user_otp
#         WHERE phone = %s
#         ORDER BY time_stamp DESC
#         LIMIT 1;
#         """
#         cursor.execute(query, (phone_number,))
#         result = cursor.fetchone()

#         cursor.close()
#         connection.close()

#         if result:
#             return result[0]
#         return None


#     @staticmethod
#     def wait_for_otp(phone_number, timeout=30):
#         """
#         Wait for OTP to be available in the database.
#         Only fetches from database - no fallback to .env file.
#         """
#         start_time = time.time()
#         attempt = 0

#         while time.time() - start_time < timeout:
#             attempt += 1
#             try:
#                 otp = OTPHelper.get_latest_otp(phone_number)

#                 if otp:
#                     print(f"✓ OTP fetched from database (attempt {attempt}): {otp}")
#                     return otp
#                 else:
#                     print(f"⏳ Waiting for OTP in database (attempt {attempt})...")
#                     time.sleep(2)

#             except Exception as exc:
#                 print(f"❌ Database error fetching OTP (attempt {attempt}): {exc}")
#                 raise

#         raise Exception(f"OTP not found in database within {timeout} seconds")