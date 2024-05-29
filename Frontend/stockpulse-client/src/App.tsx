import {
  BrowserRouter as Router,
  Route,
  Routes,
  Navigate,
} from "react-router-dom";
import Layout from "./layouts/Layout";
import Register from "./pages/Register";
import Login from "./pages/Login";
import Freemium from "./pages/freemium";
import Dashboard from "./pages/Dashboard";
import Premium from "./pages/Premium";
import CheckoutForm from "./pages/Checkout";

function App() {

  return (
    <Router>
      <Routes>
      <Route path="/" element={
          <Dashboard/>
      }/>
        <Route path="/register"
        element={
          <Layout>
            <Register/>
          </Layout>
        }/>
        <Route 
        path="/sign-in"
        element={
          <Layout>
            <Login/>
          </Layout>
        }
        />
        <Route path="/freemium"
        element={
          <Freemium/>
        }/>
        <Route path="/premium"
        element={
          <Premium/>
        }/>
        <Route path="/dashboard"
        element={
          <Dashboard/>
        }/>
         <Route path="/payment"
          element={
          <CheckoutForm />
          }
        />
        
        <Route path="*" element={<Navigate to="/" />}/>
      </Routes>
    </Router>
  )
}

export default App
