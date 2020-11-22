import { Component, OnInit } from '@angular/core';
import { FastapiService } from '../services/fastapi.service';
import { User } from '../user';

@Component({
  selector: 'app-something-cool',
  templateUrl: './something-cool.component.html',
  styleUrls: ['./something-cool.component.css']
})
export class SomethingCoolComponent implements OnInit {

  user: User;

  constructor(private fastapiService: FastapiService) { }

  ngOnInit(): void {
    this.getUserMe(); 
  }

  getUserMe(): void {
    this.fastapiService.getUserMe()
    .subscribe(user => this.user = user);
  }

}
