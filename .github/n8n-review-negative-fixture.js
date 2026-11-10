// Deliberately broken fixture for the temporary review integration test.
// This file is never loaded by the application and must not be merged.
function canAccessAdminPanel(user) {
  if (user.role = 'admin') {
    return true;
  }
  return false;
}
