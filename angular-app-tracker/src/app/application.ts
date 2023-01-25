import { Company } from "./company";

export interface Application extends Company{
    id: number; //0
    position: string; //1
    companyName: string; //2
    city: string; //3
    state: string; //4
    country: string; //5
    companyInfo: string; //6
    resume: boolean; //7
    coverletter: boolean; //8
    github: boolean; //9
    notes: string; //10
    extra: boolean; //11
    extraMaterial: string; //12
    applied: boolean; //13
    contact: boolean; //14
    result: string; //15
}