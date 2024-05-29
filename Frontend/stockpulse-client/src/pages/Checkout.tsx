import React, { useState, useEffect } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faCcVisa, faCcMastercard } from '@fortawesome/free-brands-svg-icons';
import { faRupeeSign } from '@fortawesome/free-solid-svg-icons';
import { faPaypal, faGooglePay } from '@fortawesome/free-brands-svg-icons';
import { useNavigate } from 'react-router-dom';

const CheckoutForm: React.FC = () => {
  const [termsChecked, setTermsChecked] = useState(false);
  const [showOtpNotification, setShowOtpNotification] = useState(false);
  const [otpTimer, setOtpTimer] = useState(45);
  const [showPaymentProcessingNotification, setShowPaymentProcessingNotification] = useState(false);
  const [showPaymentSuccessNotification, setShowPaymentSuccessNotification] = useState(false);

  const navigate = useNavigate();
  
  const handleTermsChange = () => {
    setTermsChecked(!termsChecked);
  };

  const handlePlaceOrder = () => {
    // Logic to send OTP
    setShowOtpNotification(true);
    const interval = setInterval(() => {
      setOtpTimer((prevTimer) => prevTimer - 1);
    }, 1000);
    setTimeout(() => {
      clearInterval(interval);
      setShowOtpNotification(false);
      setShowPaymentProcessingNotification(true);
      setTimeout(() => {
        setShowPaymentProcessingNotification(false);
        setShowPaymentSuccessNotification(true);
        setTimeout(() => {
          setShowPaymentSuccessNotification(false);
          // Redirect to "/"
          navigate("/dashboard");
        }, 2000);
      }, 3000);
    }, 8000);
  };

  const handleSubmitOtp = () => {
    // Logic to submit OTP
    setShowOtpNotification(false);
    setShowPaymentProcessingNotification(true);
    setTimeout(() => {
      setShowPaymentProcessingNotification(false);
      setShowPaymentSuccessNotification(true);
      setTimeout(() => {
        setShowPaymentSuccessNotification(false);
        // Redirect to "/"
      }, 2000);
    }, 3000);
  };

  const handleResendOtp = () => {
    // Logic to resend OTP
    setOtpTimer(45);
  };

  useEffect(() => {
    if (otpTimer === 0) {
      clearInterval();
    }
  }, [otpTimer]);

  return (
    <div className="bg-gray-100 dark:bg-gray-900">
      <div className="w-full max-w-3xl mx-auto p-8">
        <div className="bg-white dark:bg-gray-800 p-8 rounded-lg shadow-md border dark:border-gray-700">
          <h1 className="text-2xl font-bold text-gray-800 dark:text-white mb-6">Payment Gateway</h1>
          {/* Shipping Address */}
          <div className="mb-6">
            <h2 className="text-xl font-semibold text-gray-700 dark:text-white mb-2">Billing Address</h2>
            <div className="grid grid-cols-2 gap-4">
              <div>
                <label htmlFor="first_name" className="block text-gray-700 dark:text-white mb-1">First Name</label>
                <input type="text" id="first_name" className="w-full rounded-lg border py-2 px-3 dark:bg-gray-700 dark:text-white dark:border-none" />
              </div>
              <div>
                <label htmlFor="last_name" className="block text-gray-700 dark:text-white mb-1">Last Name</label>
                <input type="text" id="last_name" className="w-full rounded-lg border py-2 px-3 dark:bg-gray-700 dark:text-white dark:border-none" />
              </div>
            </div>

            <div className="mt-4">
              <label htmlFor="address" className="block text-gray-700 dark:text-white mb-1">Address</label>
              <input type="text" id="address" className="w-full rounded-lg border py-2 px-3 dark:bg-gray-700 dark:text-white dark:border-none" />
            </div>

            <div className="mt-4">
              <label htmlFor="city" className="block text-gray-700 dark:text-white mb-1">City</label>
              <input type="text" id="city" className="w-full rounded-lg border py-2 px-3 dark:bg-gray-700 dark:text-white dark:border-none" />
            </div>

            <div className="grid grid-cols-2 gap-4 mt-4">
              <div>
                <label htmlFor="state" className="block text-gray-700 dark:text-white mb-1">State</label>
                <input type="text" id="state" className="w-full rounded-lg border py-2 px-3 dark:bg-gray-700 dark:text-white dark:border-none" />
              </div>
              <div>
                <label htmlFor="zip" className="block text-gray-700 dark:text-white mb-1">ZIP Code</label>
                <input type="text" id="zip" className="w-full rounded-lg border py-2 px-3 dark:bg-gray-700 dark:text-white dark:border-none" />
              </div>
            </div>
          </div>

          {/* Payment Information */}
          <div>
            <h2 className="text-xl font-semibold text-gray-700 dark:text-white mb-2">Payment Information</h2>
            <div className="mt-4">
              <label htmlFor="card_number" className="block text-gray-700 dark:text-white mb-1">Card Number</label>
              <input type="text" id="card_number" className="w-full rounded-lg border py-2 px-3 dark:bg-gray-700 dark:text-white dark:border-none" />
            </div>

            <div className="grid grid-cols-2 gap-4 mt-4">
              <div>
                <label htmlFor="exp_date" className="block text-gray-700 dark:text-white mb-1">Expiration Date</label>
                <input type="text" id="exp_date" className="w-full rounded-lg border py-2 px-3 dark:bg-gray-700 dark:text-white dark:border-none" />
              </div>
              <div>
                <label htmlFor="cvv" className="block text-gray-700 dark:text-white mb-1">CVV</label>
                <input type="text" id="cvv" className="w-full rounded-lg border py-2 px-3 dark:bg-gray-700 dark:text-white dark:border-none" />
              </div>
            </div>
          </div>

          {/* Payment Options */}
          <div className="flex items-center justify-between mt-8">
            <FontAwesomeIcon icon={faCcVisa} className="text-5xl text-blue-500" />
            <FontAwesomeIcon icon={faCcMastercard} className="text-5xl text-red-500" />
            <FontAwesomeIcon icon={faRupeeSign} className="text-5xl text-green-500" />
            <FontAwesomeIcon icon={faGooglePay} className="text-5xl text-blue-700" />

            <FontAwesomeIcon icon={faPaypal} className="text-5xl text-blue-400" />
          </div>

          {/* Terms and Conditions */}
          <div className="flex items-center mt-4">
            <input
              type="checkbox"
              id="terms"
              checked={termsChecked}
              onChange={handleTermsChange}
              className="mr-2"
            />
            <label htmlFor="terms" className="text-gray-700 dark:text-white">
              I agree to the <a href="/terms" className="underline">Terms and Conditions</a>
            </label>
          </div>

          {/* Place Order Button */}
          <div className="mt-8 flex justify-end">
            <button
              onClick={handlePlaceOrder}
              className={`bg-teal-500 text-white px-4 py-2 rounded-lg hover:bg-teal-700 dark:bg-teal-600 dark:text-white dark:hover:bg-teal-900 ${!termsChecked && 'opacity-50 cursor-not-allowed'}`}
              disabled={!termsChecked}
            >
              Place Order
            </button>
          </div>

          {/* OTP Notification */}
          {showOtpNotification && (
            <div className="bg-blue-500 text-white p-4 mt-4 rounded-md flex justify-between items-center">
              <div>An OTP has been sent to your registered mobile number.</div>
              <div>
                <input
                  type="text"
                  placeholder="Enter OTP"
                  className="px-2 py-1 mr-2 rounded-md border text-black"

                />
                <button
                  onClick={handleSubmitOtp}
                  className={`bg-white text-blue-500 px-3 py-1 rounded-md mr-2 mb-2 ${otpTimer === 0 && 'opacity-50 cursor-not-allowed'}`}
                  disabled={otpTimer === 0}
                >
                  Submit OTP
                </button>
                <button
                  onClick={handleResendOtp}
                  className={`bg-white text-blue-500 px-3 py-1 rounded-md mr-2 mb-2 ${otpTimer > 0 && 'opacity-50 cursor-not-allowed'}`}
                  disabled={otpTimer > 0}
                >
                  Resend OTP
                </button>
                <span className="text-red-500 font-semibold">{otpTimer}s</span>
              </div>
            </div>
          )}

          {/* Payment Processing Notification */}
          {showPaymentProcessingNotification && (
            <div className="bg-green-500 text-white p-4 mt-4 rounded-md">
              Payment processing...
            </div>
          )}

          {/* Payment Success Notification */}
          {showPaymentSuccessNotification && (
            <div className="bg-green-500 text-white p-4 mt-4 rounded-md">
              Payment successfully received and the plan has been activated.
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default CheckoutForm;

