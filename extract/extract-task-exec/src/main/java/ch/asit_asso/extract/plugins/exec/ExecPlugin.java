/*
 * Copyright (C) 2017 arx iT
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
package ch.asit_asso.extract.plugins.exec;

import ch.asit_asso.extract.plugins.common.IEmailSettings;
import ch.asit_asso.extract.plugins.common.ITaskProcessor;
import ch.asit_asso.extract.plugins.common.ITaskProcessorRequest;
import ch.asit_asso.extract.plugins.common.ITaskProcessorResult;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.node.ArrayNode;
import com.fasterxml.jackson.databind.node.ObjectNode;
import java.io.File;
import java.io.IOException;
import java.lang.reflect.Field;
import java.math.BigDecimal;
import java.text.SimpleDateFormat;
import java.util.Calendar;
import java.util.Map;
import org.apache.commons.io.FileUtils;
import org.apache.commons.lang3.StringUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * A plugin that will copy data about a data item request for archiving.
 *
 * @author Florent Krin
 */
public class ExecPlugin implements ITaskProcessor {

    private static final String CONFIG_FILE_PATH = "plugins/exec/properties/configExec.properties";
    private static final String HELP_FILE_NAME = "executorHelp.html";
    private final Logger logger = LoggerFactory.getLogger(ExecPlugin.class);
    private final String code = "EXECUTE";

    /**
     * The class of the pictogram to use to represent this plugin.
     */
    private final String pictoClass = "fa-folder-open-o";

    private LocalizedMessages messages;
    private Map<String, String> inputs;
    private PluginConfiguration config;

    public ExecPlugin() {
        this.config = new PluginConfiguration(ExecPlugin.CONFIG_FILE_PATH);
        this.messages = new LocalizedMessages();
    }

    public ExecPlugin(final String language) {
        this.config = new PluginConfiguration(ExecPlugin.CONFIG_FILE_PATH);
        this.messages = new LocalizedMessages(language);
    }

    public ExecPlugin(final Map<String, String> settings) {
        this();
        this.inputs = settings;
    }

    public ExecPlugin(final String language, final Map<String, String> settings) {
        this(language);
        this.inputs = settings;
    }

    @Override
    public final ExecPlugin newInstance(final String language) {
        return new ExecPlugin(language);
    }

    @Override
    public final ExecPlugin newInstance(final String language, final Map<String, String> settings) {
        return new ExecPlugin(language, settings);
    }

    @Override
    public final String getLabel() {
        return this.messages.getString("plugin.label");
    }

    @Override
    public final String getCode() {
        return this.code;
    }

    @Override
    public final String getDescription() {
        return this.messages.getString("plugin.description");
    }

    @Override
    public final String getHelp() {
        return this.messages.getFileContent(ExecPlugin.HELP_FILE_NAME);
    }

    @Override
    public final String getPictoClass() {
        return pictoClass;
    }

    @Override
    public final String getParams() {
        ObjectMapper mapper = new ObjectMapper();
        ArrayNode parametersNode = mapper.createArrayNode();

        parametersNode.addObject()
                .put("code", this.config.getProperty("paramPath"))
                .put("label", this.messages.getString("paramPath.label"))
                .put("type", "text")
                .put("req", true)
                .put("maxlength", 255);
        parametersNode.addObject()
                .put("code", this.config.getProperty("paramTarget"))
                .put("label", this.messages.getString("paramTarget.label"))
                .put("type", "text")
                .put("req", true)
                .put("maxlength", 255);
        try {
            return mapper.writeValueAsString(parametersNode);
        } catch (JsonProcessingException exception) {
            logger.error("An error occurred when the parameters were converted to JSON.", exception);
            return null;
        }
    }

    @Override
    public final ITaskProcessorResult execute(final ITaskProcessorRequest request, final IEmailSettings emailSettings) {
        this.logger.info("Starting executor plugin: %s / %s", request, emailSettings);
        final ExecResult pluginResult = new ExecResult();
        pluginResult.setStatus(ITaskProcessorResult.Status.SUCCESS);
        pluginResult.setErrorCode("OK");
        pluginResult.setMessage(request.toString());
        pluginResult.setRequestData(request);
        return pluginResult;
    }
}
