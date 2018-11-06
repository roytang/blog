<?php /* Smarty version Smarty-3.1.14, created on 2018-02-11 17:02:44
         compiled from "/home/roytang/webapps/blog/wp-content/plugins/tsp-easy-dev/assets/templates/easy-dev-shortcode-ui.tpl" */ ?>
<?php /*%%SmartyHeaderCode:16962214435a807734935a15-87045403%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    'e8874956fbe098bc9a57b24b72f078afa8e55e3b' => 
    array (
      0 => '/home/roytang/webapps/blog/wp-content/plugins/tsp-easy-dev/assets/templates/easy-dev-shortcode-ui.tpl',
      1 => 1496120711,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '16962214435a807734935a15-87045403',
  'function' => 
  array (
  ),
  'variables' => 
  array (
    'plugin_title' => 0,
    'plugin_links' => 0,
    'plugin_name' => 0,
    'form' => 0,
    'error' => 0,
    'message' => 0,
    'form_fields' => 0,
    'field' => 0,
    'nonce_name' => 0,
  ),
  'has_nocache_code' => false,
  'version' => 'Smarty-3.1.14',
  'unifunc' => 'content_5a807734a9cd61_84559567',
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_5a807734a9cd61_84559567')) {function content_5a807734a9cd61_84559567($_smarty_tpl) {?><!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">
<!-- Optional theme -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css" integrity="sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r" crossorigin="anonymous">
<!-- Latest compiled and minified JavaScript -->
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>
<div id="tsp_wrapper">
    <div id="tsp_header" class="row">
        <div id="tsp_logo" class="col-sm-4"></div>
        <div id="tsp_links" class="col-sm-8">
        	<h4><?php echo $_smarty_tpl->tpl_vars['plugin_title']->value;?>
</h4>
        	<span><?php echo $_smarty_tpl->tpl_vars['plugin_links']->value;?>
</span>
        </div>
    </div> <!-- tsp_title -->
    <div id="tsp_content" class="row">
        <div id="tsp_tabs_list">
          <ul>
            <li><a href="#tabs-1"><i class="fa fa-cogs"></i>Shortcode Defaults</a></li>
            <li><a href="#tabs-2"><i class="fa fa-code"></i>Shortcode Instructions</a></li>
          </ul>
        </div> <!-- tsp_tabs_list -->
        <div id="tsp_tabs_content">
            <div id="tsp_tabs_inner">
                <div id="tsp_tabs_controller">
                    <div id="tabs-1">
                     	<form method="post" action="admin.php?page=<?php echo $_smarty_tpl->tpl_vars['plugin_name']->value;?>
.php" class="form-horizontal">
	                        <div id="tsp_top_bar" class="row">
						        <div id="tsp_bar_title" class="col-sm-8"><h2>Shortcode Defaults</h2></div>
						        <div id="tsp_bar_button" class="col-sm-4">
									  <div class="form-group">
										<button type="submit" class="btn btn-primary">Save Changes</button>
									  </div>
						        </div>
	                        </div>                       
	                    	<div role="alert" class="alert alert-success" <?php if (!$_smarty_tpl->tpl_vars['form']->value||$_smarty_tpl->tpl_vars['error']->value!=''){?>style="display:none;"<?php }?>><p><strong><?php echo $_smarty_tpl->tpl_vars['message']->value;?>
</strong></p></div>
	                    	<div role="alert" class="alert alert-danger" <?php if (!$_smarty_tpl->tpl_vars['error']->value){?>style="display:none;"<?php }?>><p><strong><?php echo $_smarty_tpl->tpl_vars['error']->value;?>
</strong></p></div>
	                    	<fieldset>
	                    		<?php  $_smarty_tpl->tpl_vars['field'] = new Smarty_Variable; $_smarty_tpl->tpl_vars['field']->_loop = false;
 $_from = $_smarty_tpl->tpl_vars['form_fields']->value; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array');}
foreach ($_from as $_smarty_tpl->tpl_vars['field']->key => $_smarty_tpl->tpl_vars['field']->value){
$_smarty_tpl->tpl_vars['field']->_loop = true;
?>
	                    			<?php echo $_smarty_tpl->getSubTemplate (((string)$_smarty_tpl->tpl_vars['EASY_DEV_FORM_FIELDS']->value), $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, null, null, array('field'=>$_smarty_tpl->tpl_vars['field']->value), 0);?>

	                    		<?php } ?>
                    		</fieldset>
                    		<input type="hidden" name="<?php echo $_smarty_tpl->tpl_vars['plugin_name']->value;?>
_form_submit" value="submit" />
	                        <div id="tsp_bottom_bar" class="row">
						        <div id="tsp_bar_title" class="col-sm-8"></div>
						        <div id="tsp_bar_button" class="col-sm-4">
									  <div class="form-group">
										<button type="submit" class="btn btn-primary">Save Changes</button>
									  </div>
						        </div>
	                        </div>                       
                    		<?php echo $_smarty_tpl->tpl_vars['nonce_name']->value;?>

                    	</form>
                    </div> <!-- tabs-1 -->
                    <div id="tabs-2">
                        <h2>Shortcode Instructions</h2>
        				<?php echo $_smarty_tpl->getSubTemplate (((string)$_smarty_tpl->tpl_vars['EASY_DEV_SETTINGS_UI']->value), $_smarty_tpl->cache_id, $_smarty_tpl->compile_id, null, null, array(), 0);?>

                    </div> <!-- tabs-2 -->
               </div> <!-- tsp_tabs_controller -->
            </div> <!-- tsp_tabs_inner -->
        </div> <!-- tsp_tabs_content -->
    </div> <!-- tsp_content -->
</div> <!-- tsp_wrapper -->
<?php }} ?>