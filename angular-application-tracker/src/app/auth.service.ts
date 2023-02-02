import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Auth } from './auth';

@Injectable({
  providedIn: 'root',
})
export class AuthService {

  private userURL = 'http://localhost:5001/users/';
  private token = 'key';
  private id = 'uid';

  constructor(
    private auth: Auth,
    private router: Router,
    private http: HttpClient,
  ) { }

  login(un: string, pw: string) {
    this.auth.login(un, pw).subscribe((data) => {
      localStorage.setItem(this.token, data[2]);
      localStorage.setItem(this.id, data[0]);

      console.log(data[0]);
      this.router.navigate(['/']);
    })
  }

  logout() {
    localStorage.removeItem(this.token);
    this.router.navigate(['/login']);
  }

  isLoggedIn(): boolean {
    let existToken = localStorage.getItem(this.token);
    const httpOptions = {
      headers: new HttpHeaders({ 'Content-Type': 'application/json', 'key': existToken! })};
    var valid: boolean = false;
    this.http.get<boolean>(this.userURL+this.getId(), httpOptions).subscribe(data => valid=data);
    return valid
  }

  getToken(): string | null {
    return this.isLoggedIn() ? localStorage.getItem(this.token) : null;
  }

  getId(): string {
    return localStorage.getItem(this.id)!;
  }
}
