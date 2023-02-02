import { Injectable } from '@angular/core';
import { Router } from '@angular/router';
import { Auth } from './auth';

@Injectable({
  providedIn: 'root',
})
export class AuthService {

  private token = 'key';
  private id = 'uid';

  constructor(
    private auth: Auth,
    private router: Router,
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
    return existToken != null && existToken.length > 1;
  }

  getToken(): string | null {
    return this.isLoggedIn() ? localStorage.getItem(this.token) : null;
  }

  getId(): string {
    return localStorage.getItem(this.id)!;
  }
}
