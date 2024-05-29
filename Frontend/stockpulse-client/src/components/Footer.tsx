const Footer = () => {
    return (
        <div className="bg-slate-900 py-10">
            <div className="container mx-auto flex justify-between items-center">
                <span className="text-3xl text-blue-200 font-bold tracking-tight ml-4">
                    StockPulse
                </span>
                <span className="text-white font-bold tracking-tight flex gap-4 mr-4">
                    <p className="cursor-pointer">Privacy Policy</p>
                    <p className="cursor-pointer">Terms of Service</p>
                    <p className="text-white">© 2024 All Rights Reserved</p>
                </span>
            </div>
        </div>
    );
};

export default Footer;
