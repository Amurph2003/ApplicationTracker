import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { OverviewPageComponent } from './overview-page/overview-page.component';
import { LoginComponent } from './login/login.component';
import { ApplicationComponent } from './application/application.component';
import { EditAppComponent } from './edit-app/edit-app.component';
import { FormsModule } from '@angular/forms';
import { NoExistComponent } from './no-exist/no-exist.component';

@NgModule({
  declarations: [
    AppComponent,
    OverviewPageComponent,
    LoginComponent,
    ApplicationComponent,
    EditAppComponent,
    NoExistComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    FormsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
