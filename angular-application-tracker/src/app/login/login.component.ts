import { Component, OnInit } from '@angular/core';
import { LoginService } from '../login.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(
    private loginService: LoginService,
  ) { }

  ngOnInit(): void {
  }

  login(un: string, pw: string) {
    this.loginService.postLogIn(un, pw).subscribe();
  }
}
