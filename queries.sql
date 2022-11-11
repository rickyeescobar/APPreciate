'SELECT name FROM community c JOIN community_user ON c.name = community_user.community_name WHERE community_user.user_id = ?',(g.user['id'])
);

SELECT p.id, body, created, author_id, community_name, username FROM POST p JOIN user u ON p.author_id = u.id WHERE p.community_name IN( SELECT name FROM community c JOIN community_user ON c.name = community_user.community_name WHERE community_user.user_id = 1) ORDER BY created DESC;

'SELECT p.id, body, created, author_id, community_name, username'
'FROM POST p JOIN user u ON p.author_id = u.id WHERE p.community_name '
'IN( SELECT name FROM community c JOIN community_user ON c.name = community_user.community_name '
'WHERE community_user.user_id = (?,)) ORDER BY created DESC'