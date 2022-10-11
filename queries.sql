INSERT INTO client (username, joined_on, password) VALUES('user1', '2020-02-23', 'firstpassword'), ('user2', '2017-12-10', 'secondpassword'), ('user3', '2021-04-03', 'thirdpassword');
INSERT INTO post (client_id, title, content) VALUES(5, 'First post ever', 'This is my first post ever.'), (6, 'So many posts, so little time', 'I have so much to write about that I will have to make a series of posts'), (7, 'This may be my last post', 'I have written so many posts in the past. I think I am finally done writing posts.'), 
(5, 'Wow, already at two posts', 'Thanks everyone following me on this crazy journey. I have already made it to my second post. I can still remember writing my first.'), (6, 'Part two', 'In order to have success writing so many posts it helps to have content planned well ahead of time..');

SELECT username , joined_on, password, client_id, title, content From client c INNER JOIN post p ON p.client_id = c.id; 


SELECT username, password FROM client c;

INSERT INTO post (title, content) VALUES();


CALL get_posts;


CALL get_user_posts(5); 