<?php /* Smarty version Smarty-3.1.14, created on 2017-05-31 15:00:48
         compiled from "/home/roytang/webapps/blog/wp-content/plugins/tsp-easy-dev/assets/templates/easy-dev-form-fields.tpl" */ ?>
<?php /*%%SmartyHeaderCode:182813756458991d89e8e7a0-59498202%%*/if(!defined('SMARTY_DIR')) exit('no direct access allowed');
$_valid = $_smarty_tpl->decodeProperties(array (
  'file_dependency' => 
  array (
    '79ff0c39da372fa7a3c4d06fa929e6f5e856a3cc' => 
    array (
      0 => '/home/roytang/webapps/blog/wp-content/plugins/tsp-easy-dev/assets/templates/easy-dev-form-fields.tpl',
      1 => 1496120711,
      2 => 'file',
    ),
  ),
  'nocache_hash' => '182813756458991d89e8e7a0-59498202',
  'function' => 
  array (
  ),
  'version' => 'Smarty-3.1.14',
  'unifunc' => 'content_58991d8a03f772_06945458',
  'variables' => 
  array (
    'field_prefix' => 0,
    'field' => 0,
    'class' => 0,
    'okey' => 0,
    'ovalue' => 0,
  ),
  'has_nocache_code' => false,
),false); /*/%%SmartyHeaderCode%%*/?>
<?php if ($_valid && !is_callable('content_58991d8a03f772_06945458')) {function content_58991d8a03f772_06945458($_smarty_tpl) {?><style>
.<?php echo $_smarty_tpl->tpl_vars['field_prefix']->value;?>
_url_display {
    width: 100%; 
    background-color: #FFFFFF; 
    padding: 3px; 
    border: #c6d9e9 1px solid; 
    font-size: 13px;
}
.<?php echo $_smarty_tpl->tpl_vars['field_prefix']->value;?>
_image_info
 {
	position: relative;
    margin-left: 220px;
 }
</style>
<div class="form-group <?php echo $_smarty_tpl->tpl_vars['field_prefix']->value;?>
_form_element" id="<?php echo $_smarty_tpl->tpl_vars['field']->value['name'];?>
_container_div" style="">
	<label for="<?php echo $_smarty_tpl->tpl_vars['field']->value['id'];?>
" class="col-sm-3 control-label"><?php echo $_smarty_tpl->tpl_vars['field']->value['label'];?>
</label>
	<div class="col-sm-9">
	<?php if ($_smarty_tpl->tpl_vars['field']->value['type']=='INPUT'){?>
	   <input class="<?php echo $_smarty_tpl->tpl_vars['class']->value;?>
 form-control" id="<?php echo $_smarty_tpl->tpl_vars['field']->value['id'];?>
" name="<?php echo $_smarty_tpl->tpl_vars['field']->value['name'];?>
" value="<?php echo $_smarty_tpl->tpl_vars['field']->value['value'];?>
" />
	<?php }elseif($_smarty_tpl->tpl_vars['field']->value['type']=='TEXTAREA'){?>
	   <textarea class="<?php echo $_smarty_tpl->tpl_vars['class']->value;?>
 form-control" id="<?php echo $_smarty_tpl->tpl_vars['field']->value['id'];?>
" name="<?php echo $_smarty_tpl->tpl_vars['field']->value['name'];?>
"><?php echo $_smarty_tpl->tpl_vars['field']->value['value'];?>
</textarea>
	<?php }elseif($_smarty_tpl->tpl_vars['field']->value['type']=='CHECKBOX'){?>
		<?php  $_smarty_tpl->tpl_vars['ovalue'] = new Smarty_Variable; $_smarty_tpl->tpl_vars['ovalue']->_loop = false;
 $_smarty_tpl->tpl_vars['okey'] = new Smarty_Variable;
 $_from = $_smarty_tpl->tpl_vars['field']->value['options']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array');}
foreach ($_from as $_smarty_tpl->tpl_vars['ovalue']->key => $_smarty_tpl->tpl_vars['ovalue']->value){
$_smarty_tpl->tpl_vars['ovalue']->_loop = true;
 $_smarty_tpl->tpl_vars['okey']->value = $_smarty_tpl->tpl_vars['ovalue']->key;
?>
            <?php if ($_smarty_tpl->tpl_vars['okey']->value>0){?>
                <label for="<?php echo $_smarty_tpl->tpl_vars['field']->value['id'];?>
">&nbsp;</label>
            <?php }?>
	   		<input type="checkbox" class="level-0 form-control" id="<?php echo $_smarty_tpl->tpl_vars['field']->value['id'];?>
[]" name="<?php echo $_smarty_tpl->tpl_vars['field']->value['name'];?>
[]" value="<?php echo $_smarty_tpl->tpl_vars['ovalue']->value;?>
" <?php if (is_array($_smarty_tpl->tpl_vars['field']->value['value'])&&in_array($_smarty_tpl->tpl_vars['ovalue']->value,$_smarty_tpl->tpl_vars['field']->value['value'])){?>checked<?php }?>><?php echo $_smarty_tpl->tpl_vars['ovalue']->value;?>
<br/>
		<?php } ?>
	<?php }elseif($_smarty_tpl->tpl_vars['field']->value['type']=='SELECT'){?>
	   <select class="<?php echo $_smarty_tpl->tpl_vars['class']->value;?>
 form-control" id="<?php echo $_smarty_tpl->tpl_vars['field']->value['id'];?>
" name="<?php echo $_smarty_tpl->tpl_vars['field']->value['name'];?>
" >
	   		<?php  $_smarty_tpl->tpl_vars['ovalue'] = new Smarty_Variable; $_smarty_tpl->tpl_vars['ovalue']->_loop = false;
 $_smarty_tpl->tpl_vars['okey'] = new Smarty_Variable;
 $_from = $_smarty_tpl->tpl_vars['field']->value['options']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array');}
foreach ($_from as $_smarty_tpl->tpl_vars['ovalue']->key => $_smarty_tpl->tpl_vars['ovalue']->value){
$_smarty_tpl->tpl_vars['ovalue']->_loop = true;
 $_smarty_tpl->tpl_vars['okey']->value = $_smarty_tpl->tpl_vars['ovalue']->key;
?>
	   			<option class="level-0" value="<?php echo $_smarty_tpl->tpl_vars['ovalue']->value;?>
" <?php if ($_smarty_tpl->tpl_vars['field']->value['value']==$_smarty_tpl->tpl_vars['ovalue']->value){?>selected='selected'<?php }?>><?php echo $_smarty_tpl->tpl_vars['okey']->value;?>
</option>
	   		<?php } ?>
	   </select>
	<?php }elseif($_smarty_tpl->tpl_vars['field']->value['type']=='SELECT_PAGES'){?>
	   <div id="<?php echo $_smarty_tpl->tpl_vars['field']->value['name'];?>
-box">
	   <select class="<?php echo $_smarty_tpl->tpl_vars['class']->value;?>
 form-control" id="<?php echo $_smarty_tpl->tpl_vars['field']->value['id'];?>
" name="<?php echo $_smarty_tpl->tpl_vars['field']->value['name'];?>
<?php if ($_smarty_tpl->tpl_vars['field']->value['multiple']){?>[]<?php }?>" <?php if ($_smarty_tpl->tpl_vars['field']->value['size']){?>size="<?php echo $_smarty_tpl->tpl_vars['field']->value['size'];?>
"<?php }?> <?php if ($_smarty_tpl->tpl_vars['field']->value['multiple']){?>multiple<?php }?> <?php if ($_smarty_tpl->tpl_vars['field']->value['other']){?><?php echo $_smarty_tpl->tpl_vars['field']->value['other'];?>
<?php }?>>
	   		<?php  $_smarty_tpl->tpl_vars['ovalue'] = new Smarty_Variable; $_smarty_tpl->tpl_vars['ovalue']->_loop = false;
 $_smarty_tpl->tpl_vars['okey'] = new Smarty_Variable;
 $_from = $_smarty_tpl->tpl_vars['field']->value['options']; if (!is_array($_from) && !is_object($_from)) { settype($_from, 'array');}
foreach ($_from as $_smarty_tpl->tpl_vars['ovalue']->key => $_smarty_tpl->tpl_vars['ovalue']->value){
$_smarty_tpl->tpl_vars['ovalue']->_loop = true;
 $_smarty_tpl->tpl_vars['okey']->value = $_smarty_tpl->tpl_vars['ovalue']->key;
?>
			    <?php if ($_smarty_tpl->tpl_vars['field']->value['multiple']&&is_array($_smarty_tpl->tpl_vars['field']->value['value'])){?>
	   			<option class="level-0" value="<?php echo $_smarty_tpl->tpl_vars['okey']->value;?>
" <?php if (in_array($_smarty_tpl->tpl_vars['okey']->value,$_smarty_tpl->tpl_vars['field']->value['value'])){?>selected='selected'<?php }?>><?php echo $_smarty_tpl->tpl_vars['ovalue']->value;?>
</option>
				<?php }else{ ?>
	   			<option class="level-0" value="<?php echo $_smarty_tpl->tpl_vars['okey']->value;?>
" <?php ob_start();?><?php echo $_smarty_tpl->tpl_vars['okey']->value;?>
<?php $_tmp1=ob_get_clean();?><?php if ($_smarty_tpl->tpl_vars['field']->value['value']==$_tmp1){?>selected='selected'<?php }?>><?php echo $_smarty_tpl->tpl_vars['ovalue']->value;?>
</option>
				<?php }?>
				
	   		<?php } ?>
	   </select>
	   </div>
	<?php }elseif($_smarty_tpl->tpl_vars['field']->value['type']=='IMAGE'){?>
		<input type="hidden" id="<?php echo $_smarty_tpl->tpl_vars['field']->value['id'];?>
" name="<?php echo $_smarty_tpl->tpl_vars['field']->value['name'];?>
" value="<?php echo $_smarty_tpl->tpl_vars['field']->value['value'];?>
" />
		<input type="hidden" id="<?php echo $_smarty_tpl->tpl_vars['field']->value['id'];?>
_prefix" name="<?php echo $_smarty_tpl->tpl_vars['field']->value['name'];?>
_prefix" value="<?php echo $_smarty_tpl->tpl_vars['field_prefix']->value;?>
_<?php echo $_smarty_tpl->tpl_vars['field']->value['name'];?>
" />
    	
    	<div id="<?php echo $_smarty_tpl->tpl_vars['field_prefix']->value;?>
_<?php echo $_smarty_tpl->tpl_vars['field']->value['name'];?>
_image_info" name="<?php echo $_smarty_tpl->tpl_vars['field_prefix']->value;?>
_<?php echo $_smarty_tpl->tpl_vars['field']->value['name'];?>
_image_info" class="<?php echo $_smarty_tpl->tpl_vars['field_prefix']->value;?>
_image_info">
	    	<div id="<?php echo $_smarty_tpl->tpl_vars['field_prefix']->value;?>
_<?php echo $_smarty_tpl->tpl_vars['field']->value['name'];?>
_selected_image" name="<?php echo $_smarty_tpl->tpl_vars['field_prefix']->value;?>
_<?php echo $_smarty_tpl->tpl_vars['field']->value['name'];?>
_selected_image" class="<?php echo $_smarty_tpl->tpl_vars['field_prefix']->value;?>
_selected_image">
	      		<?php if ($_smarty_tpl->tpl_vars['field']->value['value']!=''){?><img src="<?php echo $_smarty_tpl->tpl_vars['field']->value['value'];?>
" /><br/><?php }?>
	    	</div>
	    	<div name="<?php echo $_smarty_tpl->tpl_vars['field_prefix']->value;?>
_<?php echo $_smarty_tpl->tpl_vars['field']->value['name'];?>
_url_display" id="<?php echo $_smarty_tpl->tpl_vars['field_prefix']->value;?>
_<?php echo $_smarty_tpl->tpl_vars['field']->value['name'];?>
_url_display" class="<?php echo $_smarty_tpl->tpl_vars['field_prefix']->value;?>
_url_display">
	      		<?php if ($_smarty_tpl->tpl_vars['field']->value['value']!=''){?><?php echo $_smarty_tpl->tpl_vars['field']->value['value'];?>
<?php }else{ ?>No image selected<?php }?>
	    	</div>
	    	
    		<div id="<?php echo $_smarty_tpl->tpl_vars['field_prefix']->value;?>
_<?php echo $_smarty_tpl->tpl_vars['field']->value['name'];?>
_image_funcs" name="<?php echo $_smarty_tpl->tpl_vars['field_prefix']->value;?>
_<?php echo $_smarty_tpl->tpl_vars['field']->value['name'];?>
_image_funcs" class="<?php echo $_smarty_tpl->tpl_vars['field_prefix']->value;?>
_image_funcs">
		        <img src="images/media-button-image.gif" alt="Add photos from your media" /> 
				
				<a href="#" onclick="tspedev_show_media_window()" class="thickbox" title="Add an Image"> <strong>Click here to add/change your image</strong></a><br />
				<small>Note: To choose image click the "insert into post" button in the media uploader</small><br />
				
				<img src="images/media-button-image.gif" alt="Remove existing image" /> 
				<a href="#" onclick="tspedev_remove_image_url('<?php echo $_smarty_tpl->tpl_vars['field']->value['id'];?>
', 'No image selected')"><strong>Click here to remove the existing image</strong></a><br />
    		</div>
    	</div>
    	
   		<script>
			
			jQuery(document).ready(function() {
			 
				window.send_to_editor = function(html) {
				  
					imgurl = jQuery('img',html).attr('src');
			
					field_id = "<?php echo $_smarty_tpl->tpl_vars['field']->value['id'];?>
";
			
					tspedev_save_image_url(imgurl, field_id);
					tb_remove();
				}
			 
			})
			
		</script>
	<?php }?>
	</div>
	<div class="clear"></div>
	<div id="error-message-name"></div>
</div>

<?php }} ?>