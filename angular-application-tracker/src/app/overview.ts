export interface Overview {
    appID: number;
    uid: number;
    position: string;
    companyID: number;
    city: string;
    state: string;
    country: string;
    applied: boolean;
    contact: boolean;
    result: boolean;

    companyName: string;
    companyInfo: string;
    resume: boolean;
    coverletter: boolean;
    github: boolean;
    applicationNotes: string;
    extras: boolean;
    materials: string;

    deadline: string;
    appliedOn: string;
    recent: string;
    finalizedOn: string;

}