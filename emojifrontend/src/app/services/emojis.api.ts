import {HttpClient} from '@angular/common/http';
import {Injectable} from '@angular/core';
import {Observable} from 'rxjs';

@Injectable()
export class EmojiApi {
    constructor(private http: HttpClient) {}

    getEmojis(): Observable<any> {
        const url = '/getEmojis';
        return this.http.get(url);
    }
}
