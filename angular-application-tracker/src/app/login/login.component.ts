import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { tap } from 'rxjs/operators';
import { LoginService } from '../login.service';
import { User } from '../user';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  user?: User;

  constructor(
    private loginService: LoginService,
    private router: Router,
  ) { }

  ngOnInit(): void {
  }

  login(un: string, pw: string) {
    this.loginService.postLogIn(un, pw).subscribe(loggedIn => {this.user = loggedIn});
    if (this.user?.sessionKey !== 's')
      this.router.navigate(['/overview']);
  }
}
