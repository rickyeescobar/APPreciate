'SELECT name FROM community c JOIN community_user ON c.name = community_user.community_name WHERE community_user.user_id = ?',(g.user['id'])
);

