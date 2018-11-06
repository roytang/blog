<?php /* Smarty version Smarty-3.1.14, created on 2017-02-07 01:06:17
         compiled from "/home/roytang/webapps/blog/wp-content/plugins/tsp-on-this-day/templates/default_form.tpl" */ ?>
<?php /*%%SmartyHeaderCode:62042485758991d89ddbe06-60874251%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    '693207757783365c8a90a9517ba58f0d748b0bac' => 
    array (
      0 => '/home/roytang/webapps/blog/wp-content/plugins/tsp-on-this-day/templates/default_form.tpl',
      1 => 1486429437,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '62042485758991d89ddbe06-60874251',
  'function' => 
  array (
  ),
  'variables' => 
  array (
    'form_fields' => 0,
    'field' => 0,
  ),
  'has_nocache_code' => false,
  'version' => 'Smarty-3.1.14',
  'unifunc' => 'content_58991d89e075f8_85407732',
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_58991d89e075f8_85407732')) {function content_58991d89e075f8_85407732($_smarty_tpl) {?><?php  $_smarty_tpl->tpl_vars['field'] = new Smarty_Variable; $_smarty_tpl->tpl_vars['field']->_loop = false;
 $_from = $_smarty_tpl->tpl_vars['form_fields']->value; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array');}
foreach ($_from as $_smarty_tpl->tpl_vars['field']->key => $_smarty_tpl->tpl_vars['field']->value){
$_smarty_tpl->tpl_vars['field']->_loop = true;
?>
	<?php echo $_smarty_tpl->getSubTemplate (((string)$_smarty_tpl->tpl_vars['EASY_DEV_FORM_FIELDS']->value), $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, null, null, array('field'=>$_smarty_tpl->tpl_vars['field']->value), 0);?>

<?php } ?><?php }} ?>