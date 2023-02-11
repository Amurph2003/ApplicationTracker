import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit{

  constructor(
    private authService: AuthService,
    private router: Router,
  ) {}

  ngOnInit(): void {
      
  }

  login(un: string, pw: string) {
    this.authService.login(un, pw);
  }
}
