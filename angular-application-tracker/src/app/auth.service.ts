import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Observable } from 'rxjs';
import { Auth } from './auth';

@Injectable({
  providedIn: 'root',
})
export class AuthService {

  private userURL = 'https://vercel.com/amurph2003/application-tracker/GWTcR7ex69aVe8WnAYX15GUvZhLs/users/';
  private newUserURL = 'https://vercel.com/amurph2003/application-tracker/GWTcR7ex69aVe8WnAYX15GUvZhLs/user/';
  private token = 'key';
  private id = 'uid';

  constructor(
    private auth: Auth,
    private router: Router,
    private http: HttpClient,
  ) { }

  login(un: string, pw: string) {
    this.auth.login(un, pw).subscribe((data) => {
      console.log(data);
      if ((data != 'Login Unsuccessful') && (data != "Username not found")){
        localStorage.setItem(this.token, data[2]);
        localStorage.setItem(this.id, data[0]);

        console.log(data[0]);
        this.router.navigate(['/']);}
    })
  }

  logout() {
    this.auth.logout(localStorage.getItem(this.id)!)
    localStorage.removeItem(this.token);
    this.router.navigate(['/login']);
  }

  isLoggedIn() {
    let existToken = localStorage.getItem(this.token);
    if (existToken == null)
      return false
    const httpOptions = {
      headers: new HttpHeaders({ 'Content-Type': 'application/json', 'key': existToken! })};
    const Logged = this.http.get<boolean>(this.userURL+this.getId()+'/', httpOptions);
    const rV = Logged.subscribe(data => {
      console.log(data)
        if (data == true)
          return true;
        this.router.navigate(['/login']);
        return false
      })
    console.log(rV)
    return rV
    // return valid
  }

  getToken(): string | null {
    return this.isLoggedIn() ? localStorage.getItem(this.token) : null;
  }

  getId(): string {
    return localStorage.getItem(this.id)!;
  }

  register(name: string, username: string, email: string, password: string, age: number){
    const httpOptions = {
      headers: new HttpHeaders({ 'Content-Type': 'application/json' })
    };
    const userN = this.http.post(this.newUserURL, { 'name': name, 'username': username, 'email': email, 'password': password, 'age': age }, httpOptions);
    console.log(userN)
    return userN
  }
}
