import { HttpClient, HttpHeaders } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";

@Injectable({
    providedIn: 'root',
})
export class Auth {
    private loginURL = 'https://application-tracker-k6qs3y8xz-amurph2003.vercel.app/login';

    httpOptions = {
        headers: new HttpHeaders({ 'Content-Type': 'application/json' })
    };

    constructor(
        private http: HttpClient,
    ) {}

    login(username: string, password: string): Observable<string> {
        return this.http.post<string>(this.loginURL, { username: username, password: password}, this.httpOptions);
    }

    logout(uid: string) {
        console.log('h12')
        const httpOptions1 = {
            headers: new HttpHeaders({ 'Content-Type': 'application/json', 'uid': uid })
        };
        return this.http.put<string>(this.loginURL, '', httpOptions1).subscribe()
    }
}