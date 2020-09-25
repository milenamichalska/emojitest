import {HttpClient} from '@angular/common/http';
import {Injectable} from '@angular/core';
import {Observable} from 'rxjs';

@Injectable()
export class AuthApi {
    constructor(private http: HttpClient) {}

    login(username, password): Observable<any> {
        const url = '/api/token-auth/';
        return this.http.post(url, {username, password});
    }
}
