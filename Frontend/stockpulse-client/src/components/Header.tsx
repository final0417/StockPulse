import { Link } from "react-router-dom";
import { useAppContext } from "../contexts/AppContext";
import SignOutButton from "./SignOutButton";

const Header = () => {
  const {isLoggedIn}=useAppContext();
  return (
    <div className="bg-slate-900 py-6">
      <div className="container mx-auto flex items-center justify-between">
        <div className="flex items-center">
          <span className="mr-4">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
              fill="currentColor"
              className="w-12 h-10 text-blue-200 ml-4"
            >
              <path
                fillRule="evenodd"
                d="M15.22 6.268a.75.75 0 0 1 .968-.431l5.942 2.28a.75.75 0 0 1 .431.97l-2.28 5.94a.75.75 0 1 1-1.4-.537l1.63-4.251-1.086.484a11.2 11.2 0 0 0-5.45 5.173.75.75 0 0 1-1.199.19L9 12.312l-6.22 6.22a.75.75 0 0 1-1.06-1.061l6.75-6.75a.75.75 0 0 1 1.06 0l3.606 3.606a12.695 12.695 0 0 1 5.68-4.974l1.086-.483-4.251-1.632a.75.75 0 0 1-.432-.97Z"
                clipRule="evenodd"
              />
            </svg>
          </span>
          <span className="text-4xl text-blue-300 font-bold tracking-tight">
            <Link to="/">StockPulse</Link>
          </span>
        </div>
        <span className="flex space-x-4 items-center">
          {isLoggedIn ? (
            <>
              <Link
                className="flex items-center text-white text-xl px-4 py-3 font-bold hover:bg-blue-600"
                to="/investment"
              >
                Investment Playground
              </Link>
              <Link
                className="flex items-center text-white text-xl px-4 py-3 font-bold hover:bg-blue-600"
                to="/freemium"
              >
                Try Freemium
              </Link><Link
                className="flex items-center text-white text-xl px-4 py-3 font-bold hover:bg-blue-600"
                to="/premium"
              >
                Try Premium
              </Link>
              <SignOutButton />
              <div className="w-2"></div>
            </>
          ) : (
            <Link
              to="/sign-in"
              className="flex bg-white items-center text-blue-600 px-4 py-3 font-bold hover:bg-gray-100"
            >
              Sign In
              
            </Link>
            
          )}
          <div className="w-2"></div>
        </span>
      </div>
    </div>
  );
};

export default Header;
