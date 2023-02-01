import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { tap, catchError } from 'rxjs/operators';
import { User } from './user';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  private loginURL = 'http://192.168.1.163:5001/login';

  constructor(
    private http: HttpClient,
  ) { }

  postLogIn(username: string, password: string) {
    const httpOptions = {
      headers: new HttpHeaders({ 'Content-Type': 'application/json', 'username': username, 'password': password })
    };
    console.log('reached post request:', username, password);
    return this.http.post<User>(this.loginURL, { 'username': username, 'password': password }, httpOptions);

  }
}
