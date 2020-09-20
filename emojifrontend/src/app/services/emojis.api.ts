import {HttpClient} from '@angular/common/http';
import {Injectable} from '@angular/core';
import {Observable} from 'rxjs';

@Injectable()
export class EmojiApi {
    constructor(private http: HttpClient) {}

    getEmojis(query = ''): Observable<any> {
        const url = '/api/emojsSearch/?search=' + query;
        return this.http.get(url);
    }
}
