import React from "react";
import ChartOne from "../components/charts/ChartOne";
import ChartTwo from "../components/charts/ChartTwo";
import Footer from "../components/Footer";
import Header from "../components/Header";

const Dashboard: React.FC = () => {
  return (
    <>
    
      <Header/>
      <div className="container mx-auto px-4 py-8 bg-gray-900 text-white">
        {/* Search Bar */}
        <div className="flex mb-8">
          <input
            type="text"
            placeholder="Search our services..."
            className="bg-gray-700 border-2 border-gray-700 rounded-md py-2 px-4 block w-full text-white"
          />
          <button
            type="button"
            className="bg-blue-500 text-white py-2 px-4 ml-2 rounded-md"
          >
            Search
          </button>
        </div>
        <h2 className="text-blue-200 text-3xl font-bold mb-4">App Dashboard</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
          {/* Total View Count */}
<div className="bg-gray-700 p-4 rounded-lg shadow-md hover:shadow-blue-500 text-blue-500 hover:text-blue-300">
  <h3 className="text-xl font-bold mb-2">Total View Count</h3>
  <p className="text-gray-300">1000</p>
</div>
{/* Total Profit */}
<div className="bg-gray-700 p-4 rounded-lg shadow-md  hover:shadow-blue-500 text-blue-500 hover:text-blue-300">
  <h3 className="text-xl font-bold mb-2">Average Profit %</h3>
  <p className="text-gray-300">20%</p>
</div>
{/* Total Users */}
<div className="bg-gray-700 p-4 rounded-lg shadow-md  hover:shadow-blue-500 text-blue-500 hover:text-blue-300">
  <h3 className="text-xl font-bold mb-2">Total Users</h3>
  <p className="text-gray-300">50</p>
</div>
{/* Total Products */}
<div className="bg-gray-700 p-4 rounded-lg shadow-md  hover:shadow-blue-500 text-blue-500 hover:text-blue-300">
  <h3 className="text-xl font-bold mb-2">Prediction Accuracy</h3>
  <p className="text-gray-300">85%</p>
</div>
        </div>
        {/* Live Graph */}
        <div className="bg-gray-800 mt-8 p-4 rounded-lg shadow-md  hover:shadow-blue-500 text-blue-500">
          <h3 className="text-xl font-bold mb-4">Growth Graph</h3>
          {/* Add your live graph component here */}
          <ChartOne />
        </div>
        {/* Table */}
        <div className="bg-gray-800 mt-8 p-4 rounded-lg shadow-md  hover:shadow-blue-500 text-blue-500">
          <h3 className="text-xl font-bold mb-4">Sector Growth Bar</h3>
          {/* Add your table component here */}
          <ChartTwo />
        </div>
      </div>
    <Footer/>
    </>

  );
};

export default Dashboard;
