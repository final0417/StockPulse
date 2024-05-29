import { useForm } from "react-hook-form";
import { useMutation, useQueryClient } from "react-query";
import { Link, useNavigate } from "react-router-dom";
import * as apiClient from '../api-client';
import { useAppContext } from "../contexts/AppContext";

export type SignInFormData = {
    email: string;
    password: string;
};

const Login = () => {
    const { showToast}=useAppContext();
    const navigate=useNavigate();
    const queryClient=useQueryClient();
    const { register, 
        formState: { errors },
        handleSubmit
    } = useForm<SignInFormData>();

    const mutation=useMutation(apiClient.signIn,{
        onSuccess: async()=>{
            showToast({message: "Sign in Successful !",type:"SUCCESS"}),
            await queryClient.invalidateQueries("validateToken");
            navigate("/");
        },
        onError:(error:Error)=>{
            showToast({message: error.message, type:"ERROR"});
        },
    });

    const onSubmit=handleSubmit((data)=>{
        mutation.mutate(data)
    })
    return (
        <div className="flex justify-center mt-9">
            <div className="border rounded-lg p-6 ring-2 ring-blue-400 ring-opacity-75">
                <form className="flex flex-col gap-5" onSubmit={onSubmit}>
                    <h2 className=" text-blue-500 text-3xl font-bold">Sign In</h2>
                    <label className="text-white text-sm font-bold flex-1">
                        Email
                        <input
                            type="email"
                            className="border rounded w-full py-1 px-2 font-normal text-black"
                            {...register("email", { required: "This field is required" })}
                        ></input>
                        {errors.email && (
                            <span className="text-red-500">{errors.email.message}</span>
                        )}
                    </label>
                    <label className="text-white text-sm font-bold flex-1">
                        Password
                        <input
                            type="password"
                            className="border rounded w-full py-1 px-2 font-normal text-black"
                            {...register("password", {
                                required: "This field is required",
                                minLength: {
                                    value: 6,
                                    message: "Password must be at least 6 characters",
                                },
                            })}
                        ></input>
                        {errors.password && (
                            <span className="text-red-500">{errors.password.message}</span>
                        )}
                    </label>
                    <button
                        type="submit"
                        className="bg-blue-600 text-white p-2 font-bold hover:bg-blue-500 text-xl w-full"
                    >
                        Login
                    </button>
                    <span className="text-blue-200 text-sm mt-2 text-center">
                        Don't Have an account?{" "}
                        <Link to="/register" className="text-blue-400 font-bold">
                            Create Here
                        </Link>
                    </span>
                </form>
            </div>
        </div>
    );
};

export default Login;
