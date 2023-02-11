import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from '../auth.service';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.css']
})
export class SignupComponent {

  constructor(
    private authService: AuthService,
    private router: Router,
  ) {}
  
  register(name: string, username: string, email: string, password: string, age: string) {
    this.authService.register(name, username, email, password, Number(age)).subscribe(data => {
      console.log(data);
      this.authService.login(username, password);
      this.router.navigate(['/']);
    });
  }
}
