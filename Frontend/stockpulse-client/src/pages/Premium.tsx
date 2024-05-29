import React, { useState, useEffect } from "react";
import { Link, useNavigate } from "react-router-dom";

type PremiumFormData = {
    acceptTerms: boolean;
};

const Premium = () => {
    const [formData, setFormData] = useState<PremiumFormData>({
        acceptTerms: false,
    });

    const [subscriptionType, setSubscriptionType] = useState<string | null>(null);
    const [isLoading, setIsLoading] = useState(false);
    const [showSuccessNotification, setShowSuccessNotification] = useState(false);
    const [showPaymentInitiatedNotification, setShowPaymentInitiatedNotification] = useState(false);
    const [showPaymentSuccessNotification, setShowPaymentSuccessNotification] = useState(false);

    const navigate = useNavigate();

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const { name, checked } = e.target;
        setFormData((prevData) => ({
            ...prevData,
            [name]: checked,
        }));
    };

    // Function to handle subscription type selection
    const handleSubscriptionTypeSelection = (type: string) => {
        switch (type) {
            case "Monthly":
                setShowSuccessNotification(true);
                break;
            case "Yearly":
                setShowSuccessNotification(true);
                break;
            case "5-Year":
                setShowSuccessNotification(true);
                break;
            default:
                break;
        }
        setSubscriptionType(type);
    };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setIsLoading(true);
        // Simulating API call delay with setTimeout
        setTimeout(() => {
            setShowPaymentInitiatedNotification(true);
            setTimeout(() => {
                setIsLoading(false);
                setShowPaymentInitiatedNotification(false);
                    navigate("/payment");
            }, 5000);
        }, 3000);
    };

    useEffect(() => {
        // Resetting the subscription type after success notification fades out
        if (!showSuccessNotification) {
            setSubscriptionType(null);
        }
    }, [showSuccessNotification]);

    return (
        <div className="bg-gradient-to-b from-slate-600 to-slate-800 text-white shadow-2xl min-h-screen flex flex-col justify-between">
            <header className="bg-slate-900 text-yellow-300 py-4 flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="w-10 h-11 mr-2">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M12 6v12m-3-2.818.879.659c1.171.879 3.07.879 4.242 0 1.172-.879 1.172-2.303 0-3.182C13.536 12.219 12.768 12 12 12c-.725 0-1.45-.22-2.003-.659-1.106-.879-1.106-2.303 0-3.182s2.9-.879 4.006 0l.415.33M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                </svg>
                <h1 className="text-3xl font-bold text-sky-500">Premium</h1>
            </header>

            <div className="max-w-screen-xl mx-auto px-8 py-16">
                {/* Subscription Plans */}
                <div className="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8">
                    {/* Monthly Plan */}
                    <div className="border rounded-lg p-6 ring-2 ring-cyan-100 ring-opacity-75 backdrop-filter backdrop-blur-md bg-opacity-75 bg-slate-800 shadow-xl">
                        <h2 className="text-2xl font-bold text-white mb-4">Monthly Plan</h2>
                        <ul className="text-white mb-4">
                            <li>{'\u2713'} Advanced AI-generated Portfolios</li>
                            <li>{'\u2713'} Access to premium stocks and analysis</li>
                            <li>{'\u2718'} 24/7 customer support</li>
                            <li>{'\u2718'} Real-time market updates</li>
                        </ul>
                        <p className="text-white mb-4">Price: Rs 999 /month</p>
                        <button onClick={() => handleSubscriptionTypeSelection("Monthly")} className="bg-blue-700 text-white rounded-xl p-2 font-bold hover:bg-blue-600 text-xl w-full">
                            Select Monthly Plan
                        </button>
                    </div>
                    {/* Yearly Plan */}
                    <div className="border rounded-lg p-6 ring-2 ring-cyan-100 ring-opacity-75 backdrop-filter backdrop-blur-md bg-opacity-75 bg-slate-800 shadow-xl">
                        <h2 className="text-2xl font-bold text-white mb-4">Yearly Plan</h2>
                        <ul className="text-white mb-4">
                            <li>{'\u2713'} Advanced AI-generated Portfolios</li>
                            <li>{'\u2713'} Access to premium stocks and analysis</li>
                            <li>{'\u2713'} 24/7 customer support</li>
                            <li>{'\u2718'} Real-time market updates</li>
                        </ul>
                        <p className="text-white mb-4">Price: Rs 9,999 /year</p>
                        <button onClick={() => handleSubscriptionTypeSelection("Yearly")} className="bg-blue-700 text-white rounded-xl p-2 font-bold hover:bg-blue-600 text-xl w-full">
                            Select Yearly Plan
                        </button>
                    </div>
                    {/* 5-Year Plan */}
                    <div className="border rounded-lg p-6 ring-2 ring-cyan-100 ring-opacity-75 backdrop-filter backdrop-blur-md bg-opacity-75 bg-slate-800 shadow-xl">
                        <h2 className="text-2xl font-bold text-white mb-4">5-Year Plan</h2>
                        <ul className="text-white mb-4">
                            <li>{'\u2713'} Advanced AI-generated Portfolios</li>
                            <li>{'\u2713'} Access to premium stocks and analysis</li>
                            <li>{'\u2713'} 24/7 customer support</li>
                            <li>{'\u2713'} Real-time market updates</li>
                        </ul>
                        <p className="text-white mb-4">Price: Rs 39,999 /5 years</p>
                        <button onClick={() => handleSubscriptionTypeSelection("5-Year")} className="bg-blue-700 text-white rounded-xl p-2 font-bold hover:bg-blue-600 text-xl w-full">
                            Select 5-Year Plan
                        </button>
                    </div>
                </div>
                {/* Subscription Form */}
                <div className="border rounded-lg p-6 ring-2 ring-cyan-100 ring-opacity-75 backdrop-filter backdrop-blur-md bg-opacity-75 bg-slate-800 shadow-xl">
                    <form onSubmit={handleSubmit} className="flex flex-col gap-5">
                        <label className="text-white text-sm font-bold">
                            <input
                                type="checkbox"
                                name="acceptTerms"
                                checked={formData.acceptTerms}
                                onChange={handleChange}
                                className="mr-2"
                            />
                            I agree to the <Link to="/terms-and-conditions" className="underline">Terms and Conditions</Link>
                        </label>
                        <button
                            type="submit"
                            className="bg-blue-700 text-white rounded-xl p-2 font-bold hover:bg-blue-600 text-xl w-full"
                            disabled={!formData.acceptTerms}
                        >
                            {isLoading ? <i className="animate-spin text-white fas fa-spinner"></i> : "Subscribe"}
                        </button>
                    </form>
                </div>
            </div>
            {/* Notifications */}
            {/* Display notification when a plan is selected */}
            {subscriptionType && (
                <div className="bg-green-500 text-white p-3 mt-3 rounded">
                    Plan selected. Please click on subscribe and complete the payment to activate the {subscriptionType} plan.
                </div>
            )}
            {showPaymentInitiatedNotification && (
                <div className="bg-green-500 text-white p-3 mt-3 rounded">
                    Payment process initiated...
                </div>
            )}
            {/* Back to Dashboard Link */}
            <Link to="/Dashboard" className="text-white text-sm mt-2 text-center mb-8 hover:text-blue-300">
                Back to Dashboard
            </Link>
        </div>
    );
};

export default Premium;
