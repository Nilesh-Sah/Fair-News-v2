import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';

@NgModule({
  declarations: [
    AppComponent,
    // Add other components here
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,
    // Add other modules here
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
