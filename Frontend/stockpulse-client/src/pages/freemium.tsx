import { useState } from "react";
import { Link } from "react-router-dom";
import TermsAndConditions from "../components/TermsAndConditions";

type FreemiumFormData = {
    email: string;
    password: string;
    acceptFreemium: boolean;
};

const Freemium = () => {
    const [formData, setFormData] = useState<FreemiumFormData>({
        email: "",
        password: "",
        acceptFreemium: false,
    });

    const [showNotification, setShowNotification] = useState(false);
    const [showInvestmentNotification, setShowInvestmentNotification] = useState(false);

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const { name, value, type, checked } = e.target;
        const val = type === "checkbox" ? checked : value;
        setFormData((prevData) => ({
            ...prevData,
            [name]: val,
        }));
    };

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        // Your submission logic goes here
        console.log(formData);
        setShowNotification(true); // Show the green notification
        setShowInvestmentNotification(true); // Show the blue notification
    };

    return (
        <div className="bg-gradient-to-b from-slate-600 to-slate-800 text-white shadow-2xl">
            <header className="bg-slate-900 text-yellow-300 py-4 flex items-center">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="w-10 h-11 mr-2">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M12 6v12m-3-2.818.879.659c1.171.879 3.07.879 4.242 0 1.172-.879 1.172-2.303 0-3.182C13.536 12.219 12.768 12 12 12c-.725 0-1.45-.22-2.003-.659-1.106-.879-1.106-2.303 0-3.182s2.9-.879 4.006 0l.415.33M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                </svg>
                <h1 className="text-3xl font-bold text-sky-500">Freemium</h1>
            </header>

            <div className="max-w-screen-xl mx-auto px-8">
                <div className="flex justify-center items-center h-screen">
                    <div className="grid grid-cols-2 gap-6">
                        {/* Left Section */}
                        <div className="border rounded-lg p-6 ring-2 ring-cyan-100 ring-opacity-75 backdrop-filter backdrop-blur-md bg-opacity-75 bg-slate-800 shadow-xl">
                            <h2 className="text-3xl font-bold text-white">STOCKPULSE</h2>
                            <h3 className="text-xl font-semibold mt-4 mb-2 text-cyan-200">Freemium Features</h3>
                            <ul className="list-disc pl-6 text-white">
                                <li className="italic hover:bg-slate-700">These are AI generated Portfolios</li>
                                <li className="italic hover:bg-slate-700">Try the 30-days trial with us</li>
                                <li className="italic hover:bg-slate-700">10,000 pulse coins will be free initially</li>
                                <li className="italic hover:bg-slate-700">You will use demo stocks for the trial purpose for 30 days</li>
                                <li className="italic hover:bg-slate-700">Profit with the demo pulsecoin will not be added to your account</li>
                                <li className="italic hover:bg-slate-700">The portfolios are generated with only small cap stocks</li>
                                <li className="italic hover:bg-slate-700">The more time you invest, the better chances for profit</li>
                            </ul>
                        </div>
                        {/* Right Section */}
                        <div className="border rounded-lg p-6 ring-2 ring-cyan-100 ring-opacity-75 backdrop-filter backdrop-blur-md bg-opacity-75 bg-slate-800 shadow-xl">
                            <form onSubmit={handleSubmit} className="flex flex-col gap-5">
                                <label className="text-white text-sm font-bold">
                                    Email
                                    <input
                                        type="email"
                                        name="email"
                                        value={formData.email}
                                        onChange={handleChange}
                                        className="border rounded w-full py-1 px-3 font-normal bg-transparent text-white" required
                                    />
                                </label>
                                <label className="text-white text-sm font-bold">
                                    Password
                                    <input
                                        type="password"
                                        name="password"
                                        value={formData.password}
                                        onChange={handleChange}
                                        className="border rounded w-full py-1 px-2 font-normal bg-transparent text-white"
                                        required
                                    />
                                </label>
                                <div className="flex items-center">
                                    <label className="text-white text-sm font-bold mr-2">
                                        Do you want to avail freemium benefits?
                                    </label>
                                    <input
                                        type="checkbox"
                                        name="acceptFreemium"
                                        checked={formData.acceptFreemium}
                                        onChange={handleChange}
                                    />
                                </div>
                                <TermsAndConditions onAccept={() => {}} />
                                <button
                                    type="submit"
                                    className="bg-blue-700 text-white rounded-xl p-2 font-bold hover:bg-blue-600 text-xl w-full"
                                >
                                    Submit
                                </button>
                                <Link to="/dashboard" className="text-white text-sm mt-2 text-center hover:text-blue-300">
                                    Back to Dashboard
                                </Link>
                            </form>
                            {showNotification && (
                                <div className="bg-green-500 text-white p-3 mt-3 rounded">
                                    User has been successfully registered as a freemium user. Please upgrade to premium plans of your choice within 30 days. 
                                </div>
                            )}
                            {showInvestmentNotification && (
                                <div className="bg-blue-500 text-white p-3 mt-3 rounded">
                                    <a href="https://freemium-y88ji6my44x6r9eupisorz.streamlit.app/" className="underline">Click Here to view your Investment playground.</a>
                                </div>
                            )}
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
};

export default Freemium;
