-- upgrade --
CREATE TABLE IF NOT EXISTS `prod_edition` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(100) NOT NULL
) CHARACTER SET utf8mb4 COMMENT='版本表';
CREATE TABLE IF NOT EXISTS `prod_feature` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(100) NOT NULL
) CHARACTER SET utf8mb4 COMMENT='功能表';
CREATE TABLE IF NOT EXISTS `prod_permission` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(100) NOT NULL,
    `path` VARCHAR(255) NOT NULL
) CHARACTER SET utf8mb4 COMMENT='权限表';
CREATE TABLE IF NOT EXISTS `prod_sub_edition` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` VARCHAR(100) NOT NULL,
    `edition_id` INT NOT NULL
) CHARACTER SET utf8mb4 COMMENT='子版本表';
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(20) NOT NULL,
    `content` TEXT NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `prod_feature_permission` (
    `prod_feature_id` INT NOT NULL,
    `prodpermission_id` INT NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `prod_feature_subedition` (
    `prod_sub_edition_id` INT NOT NULL,
    `prodfeature_id` INT NOT NULL
) CHARACTER SET utf8mb4;
