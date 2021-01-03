import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { User } from '../user';

@Injectable({
  providedIn: 'root'
})
export class FastapiService {

  constructor(private http: HttpClient) { }

  getUserMe(): Observable<User> {
    return this.http.get<User>('https://proxy/api/user/me');
  }
}
