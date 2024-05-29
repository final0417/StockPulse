import mongoose from "mongoose";
import bcrypt from "bcryptjs"

export type UserType={
    _id:string;
    email:string;
    panNumber:string;
    password: string;
    firstName: string;
    lastName: string;
};

const userSchema=new mongoose.Schema({
    email:{type: String, required: true,unique: true},
    panNumber: {type: String, required: true},
    password: {type: String, required: true},
    firstName: {type: String,required: true},
    lastName: {type:String, required: true},
});

userSchema.pre("save", async function(next) {
    if (this.isModified('password')) {
        this.password = await bcrypt.hash(this.password, 8);
    }

    if (this.isModified('panNumber')) {
        // Masking PAN number
        const firstFiveChars = this.panNumber.substring(0, 5);
        const maskedPAN = firstFiveChars + 'XXXXX';
        this.panNumber = maskedPAN
    }
    
    next();
});

const User=mongoose.model<UserType>("User",userSchema);

export default User;

